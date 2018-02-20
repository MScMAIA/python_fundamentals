import pytest
import numpy as np

from compute import divide
from compute import multiply


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


def test_multiply():
    assert multiply(2, 2) == 4
