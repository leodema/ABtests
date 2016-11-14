import unittest

import numpy as np
from scipy.stats import ttest_ind, ttest_1samp

from ABtests.analysis.analisys import TtestIndip, Ttest1Sample


class _TestAnalysis(unittest.TestCase):
    a = [1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 3]
    b = [1, 2, 4, 3, 2, 4, 2, 1, 3, 4]


class TestAnalysis2samples(_TestAnalysis):
    def test_analysis(self):
        my_test = TtestIndip(np.array(self.a), np.array(self.b), equal_var=False)
        p_value = my_test.p_value
        t, p_value_expected = ttest_ind(self.a, self.b, equal_var=False)

        self.assertEqual(round(p_value_expected, 9), round(p_value, 9))

    def test_analysis(self):
        my_test = TtestIndip(np.array(self.a), np.array(self.b), equal_var=False)
        my_test.report_verbose(plot=True)
        self.assertEqual(round(p_value_expected, 9), round(p_value, 9))

    def test_analysis(self):
        my_test = TtestIndip(np.array(self.a), np.array(self.b), equal_var=False)
        my_test.report()

    def test_analysis_list(self):
        my_test = TtestIndip(self.a, self.b, False)
        p_value = my_test.p_value
        my_test.report()
        t, p_value_expected = ttest_ind(self.a, self.b, equal_var=False)

        self.assertEqual(round(p_value_expected, 9), round(p_value, 9))


class TestAnalysis1var(_TestAnalysis):
    mean = 5.0
    max_precision = 9

    def test_analysis(self):
        my_test = Ttest1Sample(self.mean, np.array(self.a))
        p_value = my_test.p_value
        t, p_value_expected = ttest_1samp(self.a, self.mean)

        self.assertEqual(round(p_value_expected, self.max_precision),
                         round(p_value, self.max_precision))

    def test_analysis_list(self):
        my_test = Ttest1Sample(self.mean, np.array(self.a))
        p_value = my_test.p_value
        my_test.report()
        t, p_value_expected = ttest_1samp(self.a, self.mean)

        self.assertEqual(round(p_value_expected, self.max_precision),
                         round(p_value, self.max_precision))


if __name__ == '__main__':
    unittest.main()
