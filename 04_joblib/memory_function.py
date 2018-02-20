import time

import numpy as np
from scipy.linalg import svd

from joblib import Memory

rng = np.random.RandomState(42)


def func(X, n_components=2):
    U, s, Vh = svd(X)
    return s[:n_components]


X = rng.randn(1000, 5000)

start = time.time()
func(X)
stop = time.time()
print('Elapsed time: {:.2f} s'.format(stop - start))

memory = Memory(location='cachedir', verbose=100)
func_cached = memory.cache(func)

start = time.time()
func_cached(X)
stop = time.time()
print('Elapsed time: {:.2f} s'.format(stop - start))

start = time.time()
func_cached(X)
stop = time.time()
print('Elapsed time: {:.2f} s'.format(stop - start))

X = rng.randn(1000, 5000)

start = time.time()
func_cached(X)
stop = time.time()
print('Elapsed time: {:.2f} s'.format(stop - start))
