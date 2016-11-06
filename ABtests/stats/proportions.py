import scipy.stats
import numpy as np


def z_test(successes, trials, population_mean, one_side=False):
    if type(successes) != int or type(trials) != int:
        raise TypeError
    se = population_mean * (1 - population_mean) / trials
    sd = np.sqrt(se)
    p = successes / trials
    z = (p - population_mean) / sd
    p_value = 1 - scipy.stats.norm.cdf(abs(z))
    if one_side:
        return z, 2 * p_value
    else:
        return z, p_value


def chi_square_test(prop1, prop2, axis=0):
    return scipy.stats.chisquare(prop1, prop2, axis=axis)
