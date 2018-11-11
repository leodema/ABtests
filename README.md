# ABtests

This software aims to provide an easy-to-use interface to perform AB tests analysis.


## Installation
```
pip install ABtests
```

## Usage example:

```python
import numpy as np
from  ABtests.analysis import TtestIndip

mu_test, sigma = 0, 0.1 # mean and standard deviation
mu_control = 0.2

test = np.random.normal(mu_test, sigma, 500)
control = np.random.normal(mu_control, sigma, 500)

analysis = TtestIndip(test, control)

analysis.report()

print(analysis.p_value)
```
