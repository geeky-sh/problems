import pytest


class DP:
    WAYS_CACHE = {}
    def __init__(self, coins) -> None:
        self.coins = coins

    def getWays(self, n):
        if n <= 0:
            return 0
        if n in self.WAYS_CACHE:
            return 0

        result = 0
        for coin in self.coins:
            if n - coin == 0:
                result += 1
            elif n - coin > 0:
                result += self.getWays(n-coin)
        self.WAYS_CACHE[n] = result
        return result

def _getWays(sum, coins):
    if sum < 0:
        return 0
    if not coins:
        return 0
    if len(coins) == 1 and coins[0] == sum:
        return 1

    return _getWays(sum - coins[-1], coins) + _getWays(sum, coins[0:-1])


def getWays(n: int, c: list):
    return _getWays(n, c.sort())



data = [
    (3, [8, 3, 1, 2], 3),
    (4, [1, 2, 3], 4)
]

@pytest.mark.parametrize("n, c, out", data.copy())
def test_ways(n, c, out):
    assert getWays(n, c) == out