from __future__ import division
import scipy.special as special
import numpy as np
import numpy.ma as ma
from collections import namedtuple

Ttest_1sampResult = namedtuple('Ttest_1_sample', ('statistic', 'pvalue'))
Ttest_ind = namedtuple('Ttest_indip', ('statistic', 'pvalue'))


def _chk_asarray(a, axis):
    # Always returns a masked array, raveled for axis=None
    a = ma.asanyarray(a)
    if axis is None:
        a = ma.ravel(a)
        outaxis = 0
    else:
        outaxis = axis
    return a, outaxis


def _chk2_asarray(a, b, axis):
    a = ma.asanyarray(a)
    b = ma.asanyarray(b)
    if axis is None:
        a = ma.ravel(a)
        b = ma.ravel(b)
        outaxis = 0
    else:
        outaxis = axis
    return a, b, outaxis


def ttest_1samp(population_mean, a, axis=0):
    """
    Calculates the T-test for the mean of ONE group of scores.
    Parameters
    ----------
    a : array_like
        sample observation
    population_mean : float or array_like
        expected value in null hypothesis, if array_like than it must have the
        same shape as `a` excluding the axis dimension
    axis : int or None, optional
        Axis along which to compute test. If None, compute over the whole
        array `a`.
    Returns
    -------
    statistic : float or array
        t-statistic
    pvalue : float or array
        two-tailed p-value
    Notes
    -----
    For more details on `ttest_1samp`, see `stats.ttest_1samp`.
    """
    a, axis = _chk_asarray(a, axis)
    if a.size == 0:
        return 'Empty Array'

    sample_mean = a.mean(axis=axis)
    sample_var = a.var(axis=axis, ddof=1)
    sample_count = a.count(axis=axis)
    # force df to be an array for masked division not to throw a warning
    df = ma.asanyarray(sample_count - 1.0)
    svar = ((sample_count - 1.0) * sample_var) / df
    with np.errstate(divide='ignore', invalid='ignore'):
        t = (sample_mean - population_mean) / ma.sqrt(svar / sample_count)
    prob = special.betainc(0.5 * df, 0.5, df / (df + t * t))

    return Ttest_1sampResult(t, prob)


def ttest_ind(a, b, axis=0, equal_var=True):
    """
    Calculates the T-test for the means of two independent samples of scores.
    Parameters
    ----------
    a, b : array_like
        The arrays must have the same shape, except in the dimension
        corresponding to `axis` (the first, by default).
    axis : int or None, optional
        Axis along which to compute test. If None, compute over the whole
        arrays, `a`, and `b`.
    equal_var : bool, optional
        If True, perform a standard independent 2 sample test that assumes equal
        population variances.
        If False, perform Welch's t-test, which does not assume equal population
        variance.
        .. versionadded:: 0.17.0
    Returns
    -------
    statistic : float or array
        The calculated t-statistic.
    pvalue : float or array
        The two-tailed p-value.
    Notes
    -----
    For more details on `ttest_ind`, see `stats.ttest_ind`.
    """
    a, b, axis = _chk2_asarray(a, b, axis)

    if a.size == 0 or b.size == 0:
        return 'One of the vector is empty'

    (mean1, mean2) = (a.mean(axis), b.mean(axis))
    (var1, var2) = (a.var(axis=axis, ddof=1), b.var(axis=axis, ddof=1))
    (n1, n2) = (a.count(axis), b.count(axis))

    if equal_var:
        # force df to be an array for masked division not to throw a warning
        df = ma.asanyarray(n1 + n2 - 2.0)
        svar = ((n1 - 1) * var1 + (n2 - 1) * var2) / df
        denom = ma.sqrt(svar * (1.0 / n1 + 1.0 / n2))  # n-D computation here!
    else:
        vn1 = var1 / n1
        vn2 = var2 / n2
        with np.errstate(divide='ignore', invalid='ignore'):
            df = (vn1 + vn2) ** 2 / (vn1 ** 2 / (n1 - 1) + vn2 ** 2 / (n2 - 1))

        # If df is undefined, variances are zero.
        # It doesn't matter what df is as long as it is not NaN.
        df = np.where(np.isnan(df), 1, df)
        denom = ma.sqrt(vn1 + vn2)

    with np.errstate(divide='ignore', invalid='ignore'):
        t = (mean1 - mean2) / denom
    probs = special.betainc(0.5 * df, 0.5, df / (df + t * t)).reshape(t.shape)

    return Ttest_ind(t, probs.squeeze())
