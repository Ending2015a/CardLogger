# GroupLogger

## Installation
1. Just clone this repository anywhere into your package.
```
git clone https://github.com/Ending2015a/GroupLogger.git logger
```

## Usage

```
├── main.py
└── my_module (package)
    └── logger
    └── ......
```
### Example 1
```python
# main.py
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

### Example 2
```python
# main.py
from my_module import logger
logger.Config.Use('filename'='hello.log', 'level'='DEBUG', colored=True, reset=False)

LOG = logger.getLogger('main')

# create 5 blocks
for block in range(5):
    LOG.set_header('{}th block'.format(block))
    
    # add a new row to subgroup 'None'
    LOG.add_row('row 1')
    
    # switch to subgroup 'line'
    LOG.subgroup('line')
    
    # print something out
    for line in range(block+1):
        # custom output format
        LOG.add_row('this is line', line, fmt='{}: {}')
    
    # switch to subgroup 'stars'
    LOG.subgroup('stars')
    
    # print something out
    for star in range(block+5):
        # support keyword arguments formatting
        LOG.add_row(des='star {:02d}'.format(star), stars='*' * star, fmt='{des}: {stars}')
        
    # switch back to 'None'
    LOG.subgroup()
    LOG.add_row('row 2')
    LOG.add_row('row 3')
    
    LOG.subgroup('number')
    
    # formatting
    LOG.add_row('random int', num=random.randint(132716, 36453426), fmt='{}: {num:010d}')
    LOG.add_row('random float', num=random.random(), fmt='{}: {num:8.6f}')
    
    LOG.flush(logging.INFO)  # or simply pass 'INFO'
```
