# CardLogger
CardLogger is a colorful logging module for Python.

## Installation
1. Just clone this repository into anywhere in your package.
```
git clone https://github.com/Ending2015a/CardLogger.git logger
```

## Usage

```
├── main.py
└── my_module (your package)
    └── logger    <- here
    └── ......
```
### Simple logging
```python
# main.py
from my_module import logger

logger.Config.use(filename='hello.log', level='DEBUG', colored=True, reset=False)

LOG = logger.getLogger('main')

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

### Grouped logging
```python
# main.py
from my_module import logger
logger.Config.use(filename='hello.log', level='DEBUG', colored=True, reset=False)

LOG = logger.getLogger('main')

for block in range(5):
    LOG.set_header('block {}/{}'.format(block+1, 5))

    LOG.subgroup('Items')
    LOG.add_row('item1', 10)
    LOG.add_row('item2', 3.14159265358979323846, fmt='{}: {:.5f}')
    LOG.add_row('item3', [x+block for x in range(5)])

    LOG.subgroup('Alignment')
    LOG.add_row('align', 'to', 'left', fmt='{}-{}-{}', align='l')
    LOG.add_row('align', 'to', 'center', fmt='{}-{}-{}', align='c')
    LOG.add_row('align', 'to', 'right', fmt='{}-{}-{}', align='r')
    

    LOG.subgroup('Stars')

    for i in range(5+block):
        LOG.add_row('*' * i)

    LOG.flush('INFO')

```
![](https://github.com/Ending2015a/GroupLogger/blob/master/image/screenshot2.png)


### Multi-line
* call `add_rows` to output multi-line logging
* vertical line `{|[pattern]}`, e.g. `{|*}`, `{||}`, `{|||}`
* magic font `{:@f:[font_type]}`, e.g. `{:@f:ANSI_Shadow}`
    * combine with normal spec `{:@f:ANSI_Shadow:05d}`

```python
from my_module import logger
import numpy as np

logger.Config.use(filename='hello.log', level='DEBUG', colored=True, reset=False)

LOG = logger.getLogger('main')

# numpy arrays
a = np.zeros(shape=(3, 3))
b = np.zeros(shape=(8, 4))
c = np.zeros(shape=(10, 1))
d = np.zeros(shape=(4, 4, 3))

LOG.set_header('Arrays')

caption = '''
These are numpy arrays.

The shapes from left
to right are:

* 3x3
* 8x4
* 10x1
* 4x4x3
'''

LOG.add_row('')
LOG.add_rows('My Arrays', fmt='{:@f:ANSI_Shadow}', align='center')
LOG.add_line()
LOG.add_rows(3.14159265358979323846, fmt='{:@f:Train:8.5f}', align='right')
LOG.add_line()
LOG.add_rows(caption, a=a, b=b, c=c, d=d, fmt='{} {|*} {a} {||} {b} {||} {c} {||} {d}')

LOG.flush('DEBUG')
```
![](https://github.com/Ending2015a/GroupLogger/blob/master/image/screenshot3.png)
