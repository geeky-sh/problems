import pytest

def selection_sort(nums):
    total = len(nums)
    for i in range(0, total):
        for j in range(i, total):
            if j == i or nums[j] < min_value:
                j_value, min_value = j, nums[j]

        nums[j_value] = nums[i]
        nums[i] = min_value
    return nums


data = [
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ([1, 3, 2, 4], [1, 2, 3, 4]),
    ([1, 4, 2, 3], [1, 2, 3, 4]),
    ([1, 3, 3, 1], [1, 1, 3, 3])
]

@pytest.mark.parametrize("inp, out", data)
def test_selection_sort(inp, out):
    assert selection_sort(inp) == out

