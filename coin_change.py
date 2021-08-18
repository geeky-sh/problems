import pytest


def _getWays(n: int, c: list, last):
    if last == 0:
        return 1
    elif not c:
        return 0
    elif last < 0:
        return 0
    else:
        n = last
        return _getWays(n, c[0:-1], n) + _getWays(n, c, n-c[-1])


def getWays(n: int, c: list):
    return _getWays(n, c[0:-1], n) + _getWays(n, c, n - c[-1])


data = [
    (3, [8, 3, 1, 2], 3),
    (4, [1, 2, 3], 4),
    (10, [2, 3, 5, 6], 5)
]
@pytest.mark.parametrize("n, c, out", data.copy())
def test_coin_change(n, c, out):
    assert getWays(n, c) == out