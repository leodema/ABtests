import unittest

import numpy as np

from ABtests.stats.statstest import ttest_1samp, Ttest_1sampResult


class Test_ttest_1samp(unittest.TestCase):
    mean = 4.0
    input = np.array([3, 4, 2, 3, 4, 3, 2, 3])

    def test_ttest_1samp(self):
        result = ttest_1samp(self.mean, self.input)
        self.assertEqual(result, Ttest_1sampResult(-3.7416573867739413,
                                                   0.007246989820287885))

    def test_ttest_1samp_list(self):
        result = ttest_1samp(self.mean, self.input)
        self.assertEqual(result, Ttest_1sampResult(-3.7416573867739413,
                                                   0.007246989820287885))


'''
from statsmodels.stats.proportion import proportions_ztest
z,p = proportions_ztest(returned, installs, value=.3, alternative='smaller', prop_var=.3)
print(' z-stat = {z} \n p-value = {p}'.format(z=z,p=p))
'''
if __name__ == '__main__':
    unittest.main()
