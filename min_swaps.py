"""
https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

Solution:
do a quick sort
for every swap keep a count
"""

def _minimumSwaps(low, high, arr):
    if low >= high:
        return 0
    elif low + 1 == high:
        if arr[high] < arr[low]:
            return 1
        else:
            return 0
    else:
        i, j, partition, swaps = low, high - 1, high, 0
        while i <= j and i < partition and j >= low:
            while arr[i] < arr[partition] and i < partition:
                i += 1

            while arr[j] > arr[partition] and j >= low:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
                i += 1
                j -= 1

        if i != partition:
            arr[i], arr[partition] = arr[partition], arr[i]
            swaps += 1

        return (
            swaps +
            _minimumSwaps(low, i - 1, arr) +
            _minimumSwaps(i + 1, high, arr)
        )


def minimumSwaps(arr):
    return _minimumSwaps(0, len(arr) - 1, arr)


def test_fun():
    assert minimumSwaps([4, 3, 1, 2]) == 3
    assert minimumSwaps([2, 3, 4, 1, 5]) == 3
    assert minimumSwaps([1, 2, 3, 4]) == 0