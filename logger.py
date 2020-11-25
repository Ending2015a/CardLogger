# --- built in ---
import os
import sys
import time
import logging

from logging.config import dictConfig
from collections import OrderedDict
from string import Formatter


LOG_FORMAT = '[%(asctime)s|%(threadName)s|%(levelname)s|%(name)s:%(filename)s:%(lineno)d]: %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

ROOT_NAME = __name__.split('.', 1)[0]
MODULE_PATH = __name__.rsplit('.', 1)[0]
formatter_module = __import__(MODULE_PATH+'.formatter', fromlist=['.'])

MultilineStringFormatter = getattr(formatter_module, 'MultilineStringFormatter')


COLORED_LOG_FORMAT = '$TIME%(asctime)s$RESET $THREAD%(threadName)s$RESET $LEVEL[%(levelname)s]$RESET $MODULE%(name)s:%(filename)s:%(lineno)d$RESET: $LEVEL%(message)s$RESET'


def makedirs(path):
    if not path:
        return
    try:
        os.makedirs(path)
    except OSError as e:
        import errno
        if e.errno != errno.EEXIST:
            raise


def _exists(name):
    '''
    Check if a logger exists
    '''
    return name in logging.Logger.manager.loggerDict


def exists(name=None, prefix=ROOT_NAME):
    if name is not None:
        name = '.'.join([prefix, name])
    else:
        name = prefix

    return _exists(name)


def getLogger(name=None, level=None, prefix=ROOT_NAME):
    if name is not None:
        name = '.'.join([prefix, name])
    else:
        name = prefix


    # if the logger does not exist, nad no level is specified, then use default level (DEBUG)
    if (level is None) and (not _exists(name)):
        level = 'DEBUG' 

    logger = logging.getLogger(name)

    if not (level is None):
        logger.setLevel(logging.getLevelName(level))

    return logger




class CardLogger(logging.Logger):
    
    #'======= Epoch 5/10 ======='
    #'|------- Training -------|'
    #'| loss: 100.0            |'
    #'| entropy: 1132121.456   |'
    #'|--------- Eval ---------|'
    #'| loss: 2121.17455       |'
    #'=========================='

    _alignment_abbreviation = {'l': 'left', 'c': 'center', 'r': 'right'}

    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)

        self.header = None
        self.groups = OrderedDict()
        self.groups['None'] = []
        self.current_group = 'None'

    def set_header(self, name=None):
        if not isinstance(name, str):
            raise ValueError('Header name must be a str type')
        self.header = name

    def subgroup(self, name=None):

        if name is None:
            name = 'None'

        if not isinstance(name, str):
            raise ValueError('Group name must be str type')

        self.current_group = name

    def add_row(self, *args, fmt=None, align='left', **kwargs):
        if not self.current_group in self.groups:
            self.groups[self.current_group] = []

        if align in self._alignment_abbreviation:
            align = self._alignment_abbreviation[align]

        assert align in ['left', 'center', 'right']

        self.groups[self.current_group].append( (args, kwargs, fmt, False, align, False) )

    def add_rows(self, *args, fmt=None, align='left', **kwargs):
        if not self.current_group in self.groups:
            self.groups[self.current_group] = []

        if align in self._alignment_abbreviation:
            align = self._alignment_abbreviation[align]
        
        assert align in ['left', 'center', 'right']

        self.groups[self.current_group].append( (args, kwargs, fmt, True, align, False) )

    def add_line(self):
        
        # args, kwargs, fmt, Multiline, align, horizontal line
        self.groups[self.current_group].append( (None, None, None, False, None, True) )

    def clear(self):
        self.header = None
        self.groups = OrderedDict()
        self.groups['None'] = []
        self.current_group = 'None'

    def _create_header(self, width):
        if self.header is None:
            header = '=' * width

        else:
            half = (width - len(self.header)) // 2 - 1
            header = ' '.join(['=' * half, self.header, '=' * half])

        return header

    def _create_tail(self, width):
        return '=' * width

    def _create_subheader(self, name, width):

        remain = width - len(name)
        l_half = remain // 2
        r_half = remain - l_half

        l_half -= 2
        r_half -= 2

        subheader = ''.join(['|', '-'*l_half, ' ', name, ' ', '-'*r_half, '|'])

        return subheader

    def _create_row(self, string, align, width):
        remain = width - len(string) - 4

        if align == 'center':
            l = remain//2
            r = remain - l
        elif align == 'left':
            l = 0
            r = remain
        else: #right
            r = 0
            l = remain

        return ''.join(['| ', ' '*l, string, ' '*r, ' |'])

    def _create_line(self, width):
        remain = width - 2 # | + ----- + |

        return ''.join([ '|', '-'*remain, '|' ])

    def _format_contents(self):
        '''
        Formatting contents
        '''
        
        group_str = OrderedDict()

        max_length = 0

        # compute max row length
        for group, rows in self.groups.items():

            if group not in group_str:
                group_str[group] = []

            for row in rows:
                args = row[0]
                kwargs = row[1]
                fmt = row[2]
                multi_line = row[3]
                align = row[4]
                line = row[5]


                if line:
                    # string, align, horizontal line
                    group_str[group].append((None, None, True))
                    continue

                if not multi_line:

                    if fmt is None:
                        if len(args) > 0:
                            fmt = '{}'
                            if len(args) > 1:
                                fmt += ': ' + ', '.join(['{}' for _ in range(len(args[1:]))])
                        else:
                            fmt = ''

                    string = fmt.format(*args, **kwargs)

                    group_str[group].append( (string, align, False) )
                
                    max_length = max(max_length, len(string))

                else:
                    # print multi line

                    if fmt is None:
                        if len(args) > 0:
                            fmt = '{}'
                            if len(args) > 1:
                                fmt += ': ' + ', '.join(['{}' for _ in range(len(args[1:]))])
                        else:
                            fmt = ''

                    strings = MultilineStringFormatter().format(fmt, *args, **kwargs)

                    for line in strings:
                        group_str[group].append( (line, align, False) )
                        max_length = max(max_length, len(line))

        # calculate max length
        max_width = max_length + len('|  |')

        # calculate max sub header length
        for group in self.groups.keys():
            group_width = len(group) + len('|-  -|')

            max_width = max(max_width, group_width)

        if self.header is not None:
            header_width = len(self.header) + len('=====  =====')

            max_width = max(max_width, header_width)

            if (max_width - len(self.header)) % 2 > 0:
                max_width += 1


        # formatting message
        messages = []
        messages.append(self._create_header(max_width))

        for group, contents in group_str.items():

            if len(contents) == 0:
                continue

            if group is not 'None':
                messages.append(self._create_subheader(group, max_width))

            for content in contents:
                string = content[0]
                align = content[1]
                line = content[2]
                # horizontal line
                if line:
                    messages.append(self._create_line(max_width))
                else:
                    messages.append(self._create_row(string, align, max_width))

        messages.append(self._create_tail(max_width))
            
        return messages
    

    def flush(self, level=logging.INFO, 
                    tostring=None, 
                    tolist=None, 
                    new_line=True,
                    contents=None):
        '''
        Flush content
        
        args:
            tostring: convert to a single string
            tolist: convert to a list of strings
            new_line: add a new line after the contents
            contents: a str or a list of str
        '''


        if isinstance(level, str):
            level = logging.getLevelName(level)

        if not isinstance(level, int):
            if logging.raiseExceptions:
                raise TypeError('level must be an integer or string')
            else:
                return
        
        if self.isEnabledFor(level):
        
            if contents is not None:
            
                assert isinstance(contents, (str, list)), 'The contents must be a str or a list of str'
                
                if isinstance(contents, str):
                    contents = contents.split('\n')
            else:
                contents = self._format_contents()
                
            
            assert isinstance(contents, list)
            
            # add a new line
            if new_line:
                contents.append('')
                
                
            assert not (tostring and tolist), 'tostring and tolist, only one can be True'
            
            # convert to list
            if tolist:
                self.clear()
                return contents
                
            # convert to string
            if tostring:
                contents = '\n'.join(contents)
                self.clear()
                return contents
                
            # output to log
            for c in contents:
                self._log(level, c, None)


            '''
            self._log(level, self._create_header(max_width), None)

            for group, contents in group_str.items():

                if len(contents) == 0:
                    continue

                if group is not 'None':

                    self._log(level, self._create_subheader(group, max_width), None)

                for content in contents:
                    string = content[0]
                    align = content[1]
                    line = content[2]
                    # horizontal line
                    if line:
                        self._log(level, self._create_line(max_width), None)
                    else:
                        self._log(level, self._create_row(string, align, max_width), None)

            self._log(level, self._create_tail(max_width), None)
            self._log(level, '', None)
            '''

        self.clear()
        
        if tostring:
            return ''
        if tolist:
            return []


class LoggingConfig:
    def __init__(self, filename=None, level='INFO', colored=True, **kwargs):

        '''
        args:
            filename: logging file name. It will not save to file if it is 'None'
            level: logging level on console. The logging level saving to file is always set to 'DEBUG'
            colored: colored console log
        kwargs:
            reset: reset loggers. Setting this to True will disable all existed loggers
        '''
        
        console_formatter = ROOT_NAME+'-colored' if colored else ROOT_NAME

        output_to_file = not (filename is None)
        
        if output_to_file:

            path = os.path.dirname(filename)
            makedirs(path)


        config = {
            'version': 1,
            'formatters': {
                ROOT_NAME+'-colored': {
                    '()': MODULE_PATH+'.ColoredFormatter',
                    'format': COLORED_LOG_FORMAT,
                    'datefmt': LOG_DATE_FORMAT,
                },
                ROOT_NAME: {
                    'format': LOG_FORMAT,
                    'datefmt': LOG_DATE_FORMAT,
                }
            },
            'handlers': {
                'console': {
                    'level': level,
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://sys.stdout',
                    'formatter': console_formatter,
                },
            },
            'loggers': {
                ROOT_NAME: {
                    'handlers': ['console'] ,
                    'level': 'DEBUG',
                    'propagate': False,
                }
            }
        }

        if output_to_file:
            config['handlers'][filename] = {
                'level': 'DEBUG',
                'filename': filename,
                'class': 'logging.FileHandler',
                'formatter': ROOT_NAME
            }

            config['loggers'][ROOT_NAME]['handlers'] += [filename]


        self.config = config



    def apply(self, reset=False):
        '''
        Apply configurations

        reset: reset logger. Setting this to True will disable all existing loggers.
        '''


        self.config['disable_existing_loggers'] = reset
        dictConfig(self.config)

    @classmethod
    def use(cls, **kwargs):
        reset = kwargs.pop('reset', False)

        conf = cls(**kwargs)
        conf.apply(reset=reset)

        return conf


logging.setLoggerClass(CardLogger)

__all__ = [
    LoggingConfig.__name__,
]
