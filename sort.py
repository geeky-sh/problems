import pytest

def selection_sort(nums):
    total = len(nums)
    for i in range(0, total):
        min_idx = i
        for j in range(i+1, total):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[min_idx], nums[i] = nums[i], nums[min_idx]
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

