import pytest
import numpy as np
from numpy.testing import assert_allclose

from compute import divide
from compute import multiply

rng = np.random.RandomState(42)


@pytest.mark.parametrize(
    "a, b, x, dtype",
    [(1, 2, 0.5, np.float64),
     (4, 2, 2, np.float64)])
def test_divide(a, b, x, dtype):
    res = divide(a, b)
    assert res == pytest.approx(x)
    assert np.dtype(type(res)) == dtype


def test_divide_zero():
    x = divide(2, 0)
    assert np.isinf(x)


@pytest.mark.parametrize(
    "a, b, x",
    [(np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([0.25, 0.4, 0.5])),
     (rng.randn(3), rng.randn(3), np.array([0.326136, 0.590486, -2.766281]))]
)
def test_divide_array(a, b, x):
    assert_allclose(divide(a, b), x, rtol=1e-4)


def test_multiply():
    assert multiply(2, 2) == 4
