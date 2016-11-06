import numpy as np
from matplotlib import pyplot
import seaborn as sns

def myplot(x, y):
    x, y = np.array(x), np.array(y)

    # bins = np.linspace(-10, 10, 100)
    x1 = sns.kdeplot(x, shade=True)
    x2 = sns.kdeplot(y, shade=True)
    x1.set_xlabel('Value')
    x2.set_ylabel('Percentage')
    # pyplot.hist(x, bins, alpha=0.5, label='x')
    # pyplot.hist(y, bins, alpha=0.5, label='y')

    pyplot.legend(loc='upper right')
    pyplot.title('Cumulative distributions')
    pyplot.show()
