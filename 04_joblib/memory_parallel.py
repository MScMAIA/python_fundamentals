import time

from joblib import Parallel, Memory, delayed


memory = Memory(location='cachedir', verbose=100)


def func(x):
    time.sleep(4)
    return x


start = time.time()
for x in [2, 5]:
    func(x)
stop = time.time()
print('\n Elapsed time {:.2f} s'.format(stop - start))

start = time.time()
res = Parallel(n_jobs=2)(delayed(func)(x)
                         for x in [2, 5])
stop = time.time()
print('\n Elapsed time {:.2f} s'.format(stop - start))

start = time.time()
res = Parallel(n_jobs=2)(delayed(func)(x)
                         for x in [2, 5, 8])
stop = time.time()
print('\n Elapsed time {:.2f} s'.format(stop - start))

func_cached = memory.cache(func)

start = time.time()
res = Parallel(n_jobs=2)(delayed(func_cached)(x)
                         for x in [2, 5])
stop = time.time()
print('\n Elapsed time {:.2f} s'.format(stop - start))

start = time.time()
res = Parallel(n_jobs=2)(delayed(func_cached)(x)
                         for x in [2, 5, 8, 10])
stop = time.time()
print('\n Elapsed time {:.2f} s'.format(stop - start))

start = time.time()
res = Parallel(n_jobs=2)(delayed(func_cached)(x)
                         for x in [2, 5, 8, 10])
stop = time.time()
print('\n Elapsed time {:.2f} s'.format(stop - start))

memory.clear()
