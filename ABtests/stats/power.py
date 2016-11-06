from __future__ import division
import statsmodels.stats.power as smp


def calculate_power(difference, n_observation, alpha=0.05, alternatives='smaller'):
    return smp.ttest_power(difference, nobs=n_observation, alpha=alpha, alternative=alternatives)

def calculate_sample_size():
    smp.tt_ind_solve_power
    pass

