import numpy as np


def bootstrap(v, sample_size=1000, n_samples=1000):
    return [np.random.choice(v, sample_size).mean() for _ in range(n_samples)]