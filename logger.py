import os
import sys
import time
import logging

from logging.config import dictConfig


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


def getLogger(name=None, level='DEBUG', prefix=ROOT_NAME):
    if name is not None:
        name = '.'.join([prefix, name])
    else:
        name = prefix

    logger = logging.getLogger(name)
    logger.setLevel(logging.getLevelName(level))

    return logger



class LoggingConfig:
    def __init__(self, filename=None, level='INFO', **kwargs):

        '''
        filename: logging file name. It will not save to file if it is 'None'
        level: logging level on console. The logging level saving to file is always set to 'DEBUG'
        colored: colored console log
        reset: reset loggers. Setting this to True will disable all existed loggers
        '''

        colored = kwargs.get('colored', False)

        
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



__all__ = [
    LoggingConfig.__name__,
]
