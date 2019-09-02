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
    @staticmethod
    def Use(filename=None, level='INFO', **kwargs):

        console_formatter = ROOT_NAME+'-colored' if kwargs.get('colored', False) else ROOT_NAME

        output_to_file = not (filename is None)
        
        if output_to_file:

            path = os.path.dirname(filename)
            makedirs(path)


        config = {
            'version': 1,
            'disable_existing_loggers': False,
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
                PARENT_NAME: {
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

            config['loggers'][PARENT_NAME]['handlers'] += [filename]


        dictConfig(config)

__all__ = [
    LoggingConfig.__name__,
]
