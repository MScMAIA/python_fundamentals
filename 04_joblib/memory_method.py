import time

import numpy as np
from scipy.linalg import svd

from joblib import Memory

rng = np.random.RandomState(42)


def _func(X, n_components):
    U, s, Vh = svd(X)
    return X[:n_components]


class Algorithm(object):

    def __init__(self, n_components=2, memory=None):
        self.n_components = n_components
        self.memory = memory

    def extract(self, X):
        if self.memory is not None:
            func_cached = self.memory.cache(_func)
        else:
            func_cached = _func
        return func_cached(X, self.n_components)


X = rng.randn(1000, 5000)
alg = Algorithm()

start = time.time()
alg.extract(X)
stop = time.time()
print('Elapsed time: {:.2f} s'.format(stop - start))

alg = Algorithm(memory=Memory(location='cachedir', verbose=100))

start = time.time()
alg.extract(X)
stop = time.time()
print('Elapsed time: {:.2f} s'.format(stop - start))

start = time.time()
alg.extract(X)
stop = time.time()
print('Elapsed time: {:.2f} s'.format(stop - start))
