# --- built in ---
import os
import sys
import time
import logging

from logging.config import dictConfig
from collections import OrderedDict



LOG_FORMAT = '[%(asctime)s|%(threadName)s|%(levelname)s|%(name)s:%(filename)s:%(lineno)d]: %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

ROOT_NAME = __name__.split('.', 1)[0]
MODULE_PATH = __name__.rsplit('.', 1)[0]

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




class GroupLogger(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        super(GroupLogger, self).__init__(name, level)

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

    def add_row(self, *args, fmt=None, **kwargs):
        if not self.current_group in self.groups:
            self.groups[self.current_group] = []

        self.groups[self.current_group].append( (args, kwargs, fmt, False) )

    def add_rows(self, key, value, fmt=None):
        if not self.current_group in self.groups:
            self.groups[self.current_group] = []

        self.groups[self.current_group].append( ([key, value], None, fmt, True) )

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

        #'======= Epoch 5/10 ======='
        #'|------- Training -------|'
        #'| loss: 100.0            |'
        #'| entropy: 1132121.456   |'
        #'|--------- Eval ---------|'
        #'| loss: 2121.17455       |'
        #'=========================='

        remain = width - len(name)
        l_half = remain // 2
        r_half = remain - l_half

        l_half -= 2
        r_half -= 2

        subheader = ''.join(['|', '-'*l_half, ' ', name, ' ', '-'*r_half, '|'])

        return subheader

    def _create_row(self, string, width):
        remain = width - len(string) - 4

        return ''.join(['| ', string, ' '*remain, ' |'])

    def flush(self, level=logging.INFO):
        
        group_str = OrderedDict()

        max_length = 0

        # compute max row length
        for group, rows in self.groups.items():

            if group not in group_str:
                group_str[group] = []

            for row in rows:
                kargs = row[0]
                kwargs = row[1]
                fmt = row[2]
                multi_line = row[3]

                if not multi_line:

                    if fmt is None:
                        fmt = '{}'
                        if len(kargs) > 1:
                            fmt += ': ' + ', '.join(['{}' for _ in range(len(kargs[1:]))])

                    string = fmt.format(*kargs, **kwargs)

                    group_str[group].append(string)
                
                    max_length = max_length if len(string) < max_length else len(string)

                else:
                    # print multi line

                    if fmt is None:
                        fmt = '{}'
                        if len(kargs) > 1:
                            fmt += ': ' + ', '.join(['{}' for _ in range(len(kargs[1:]))])

                    # 'aa\naaa', 'bbb\nbbbbb\ncc'
                    kargs = [ str(arg).split('\n') for arg in kargs ]
                    # ['aa', 'aaa'], ['bbb', 'bbbbb', 'cc']

                    max_line_count = max(map(lambda x:len(x), kargs))
                    # 3

                    # '{}: {}'
                    fmt_segments = fmt.split('{')
                    # ['', '}: ', '}']

                    strings = [fmt_segments[0] for _ in range(max_line_count)] # the format for each line



                    strings_max_length = 0
                    for idx, arg in enumerate(kargs):
                        
                        
                        # for each arg segments (each line)
                        for _idx, seg in enumerate(arg):
                            strings[_idx] += seg
                            strings_max_length = strings_max_length if len(strings[_idx]) < strings_max_length else len(strings[_idx])

                        # pad
                        for _idx in range(len(strings)):
                            strings[_idx] += ' ' * (strings_max_length - len(strings[_idx])) # pad to same length with spaces

                        # add next fmt segments
                        if len(fmt_segments) >= idx+1:
                            for _idx, _ in enumerate(strings):
                                if _idx == 0:
                                    strings[_idx] += fmt_segments[idx+1].replace('}', '')
                                else:
                                    strings[_idx] += ' ' * len(fmt_segments[idx+1])


                    for string in strings:
                        group_str[group].append(string)
                        max_length = max_length if max_length > len(string) else len(string) 


        max_width = max_length + len('|  |')

        # compute max sub header length
        for group in self.groups.keys():
            group_width = len(group) + len('|-  -|')

            max_width = max_width if group_width < max_width else group_width

        if self.header is not None:
            header_width = len(self.header) + len('=====  =====')

            max_width = max_width if header_width < max_width else header_width

            if (max_width - len(self.header)) % 2 > 0:
                max_width += 1


        if isinstance(level, str):
            level = logging.getLevelName(level)

        if not isinstance(level, int):
            if logging.raiseExceptions:
                raise TypeError('level must be an integer or string')
            else:
                return


        # output to log
        if self.isEnabledFor(level):
            self._log(level, self._create_header(max_width), None)

            for group, strings in group_str.items():

                if len(strings) == 0:
                    continue

                if group is not 'None':

                    self._log(level, self._create_subheader(group, max_width), None)

                for contant in strings:
                    self._log(level, self._create_row(contant, max_width), None)

            self._log(level, self._create_tail(max_width), None)
            self._log(level, '', None)

        self.clear()


class LoggingConfig:
    def __init__(self, filename=None, level='INFO', colored=True, **kwargs):

        '''
        filename: logging file name. It will not save to file if it is 'None'
        level: logging level on console. The logging level saving to file is always set to 'DEBUG'
        colored: colored console log
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



    def Apply(self, reset=False):
        '''
        Apply configurations

        reset: reset logger. Setting this to True will disable all existing loggers.
        '''


        self.config['disable_existing_loggers'] = reset
        dictConfig(self.config)

    @classmethod
    def Use(cls, **kwargs):
        reset = kwargs.pop('reset', False)

        conf = cls(**kwargs)
        conf.Apply(reset=reset)

        return conf


logging.setLoggerClass(GroupLogger)

__all__ = [
    LoggingConfig.__name__,
]
