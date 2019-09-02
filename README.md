# logger

## Installation
1. Just put this repository anywhere in your package.

## Usage

```python
import my_module.logger

my_module.logger.Config.Use(filename='hello.log', level='DEBUG', colored=True)

LOG = my_module.logger.getLogger('main')

LOG.debug('hello, debug')
LOG.info('hello, info')
LOG.warning('hello, warning')
LOG.error('hello, error')

try:
    1/0
except:
    LOG.exception('hello, exception')
```

![](https://github.com/Ending2015a/logger/blob/master/image/screenshot.png)
