from _pytest.pytester import LsofFdLeakChecker
import pytest

def _knapsack(total, weights, values, last):
    if last < 0:
        return 0
    if total <= 0:
        return 0

    b = -1
    if weights[last] == total:
        b = values[last]
    elif weights[last] <= total:
        b = values[last] + _knapsack(total-weights[last], weights, values, last-1)
    a = _knapsack(total, weights, values, last - 1)

    result = max(a, b)
    return result

def knapsack(total, weights, values):
    return _knapsack(total, weights, values, len(weights) - 1)


data = [
    (7, [1, 3, 4, 5], [1, 4, 5, 7], 9),
]
@pytest.mark.parametrize("total, weights, values, out", data.copy())
def test_knapsack(total, weights, values, out):
    assert knapsack(total, weights, values) == out