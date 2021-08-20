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

def iter_knapsack(total, weights, values):
    result = []
    for i in range(0, len(weights)):
        result.append([0]*(total+1))

    for i in range(0, len(weights)):
        for j in range(0, total + 1):
            if j == 0:
                result[i][j] = 0
            else:
                i_weight = weights[i]
                i_value = values[i]
                a, b = 0, 0
                if j >= i_weight:
                    a = i_value
                    diff = j - i_weight
                    if diff >= 0 and i > 0:
                        a += result[i-1][diff]
                if i> 0:
                    b = result[i-1][j]
                print(i, i)
                result[i][j] = max(a, b)

    return result[i][j]





data = [
    (7, [1, 3, 4, 5], [1, 4, 5, 7], 9),
]
# @pytest.mark.parametrize("total, weights, values, out", data.copy())
# def test_knapsack(total, weights, values, out):
#     assert knapsack(total, weights, values) == out

@pytest.mark.parametrize("total, weights, values, out", data.copy())
def test_iter_knapsack(total, weights, values, out):
    assert iter_knapsack(total, weights, values) == out
