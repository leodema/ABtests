'''
These functions are almost identical of the ones in statsmodels

[1] statsmodels.sourceforge.net
'''
import numpy as np
import pandas as pd

from ABtests import stats
from ABtests.stats import calculate_power
from utility import myplot


class StatPower(object):
    def __init__(self, data=None, n_observations=None):
        self.data = data
        self.n_observations = n_observations


class _Ttest_builder(object):
    def plot(self):
        myplot(self.a, self.b)

    def report(self, plot=False, significance=0.05):
        data = {'Mean Control': [self.mean_a],
                'Mean Test': [self.mean_b],
                'Difference': [self.difference_means],
                'P-Value': [self.p_value],
                'Significance': [significance > self.p_value],
                'Power': [self.power],
                'Percentage Difference': ['{:4.2f}%'.format(self.difference_means_perc)]}
        report_table = pd.DataFrame(data, index=['Results'])
        if plot:
            plot()
        print(report_table)

    def report_verbose(self, plot=False, significance=0.05):
        print('-' * 20)
        print('T-test for two independent samples with {}'
              .format('equal variance' if self.equal_var is True else 'unequal Variance\n'))
        print('p-value: {p_value:.4f}, statistic {statistic:.4f} '.format(p_value=self.p_value,
                                                                          statistic=self.statistic))
        if self.p_value > significance:
            print('Not statistically significant at {significance}\n'.format(significance=significance))
        else:
            print('Statistically significant at {significance}\n'.format(significance=significance))

        print('Power: {power:.4f}'.format(power=self.power))

        if self.power > 0.8:
            print('Enough power\n'.format(significance=significance))
        else:
            print('Not enough power\n'.format(significance=significance))

        if plot:
            myplot(self.a, self.b)


class TtestIndip(_Ttest_builder):
    def __init__(self, a, b, equal_var=True):
        self.a = np.array(a)
        self.b = np.array(b)
        self.mean_a = self.a.mean()
        self.mean_b = self.b.mean()
        self.equal_var = equal_var
        self.statistic, self.p_value = stats.ttest_ind(self.a, self.b, equal_var=self.equal_var)
        self.difference_means = self.mean_a - self.mean_b
        self.difference_means_perc = self.difference_means / self.mean_a
        self.power = calculate_power(difference=self.difference_means_perc, n_observation=len(self.b))


class Ttest1Sample(_Ttest_builder):
    def __init__(self, population_mean, b):
        self.b = np.array(b)
        self.population_mean = population_mean
        self.mean_a = population_mean
        self.mean_b = b.mean()
        self.equal_var = True
        self.statistic, self.p_value = stats.ttest_1samp(self.population_mean, self.b)
        self.difference_means = self.mean_a - self.mean_b
        self.difference_means_perc = self.difference_means / self.mean_a
        self.power = calculate_power(difference=self.difference_means_perc, n_observation=len(self.b))

def test_proportions():
    print(stats.chi_square_test([16, 18, 16, 14, 12, 12], [16, 16, 16, 16, 16, 8]))
    return (stats.chi_square_test(0.2, 0.3))
