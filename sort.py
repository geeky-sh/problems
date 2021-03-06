import re
import ipdb
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


def bubble_sort(nums):
    iterations = len(nums)
    successful_pass = False
    while iterations > 0 and not successful_pass:
        successful_pass = True
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                successful_pass = False
        iterations -= 1
    return nums

def _sorted_sort(a, b):
    i, j = 0, 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        elif b[j] < a[i]:
            result.append(b[j])
            j += 1
        else:
            result.append(a[i])
            result.append(b[j])
            i += 1
            j += 1

    if i == len(a):
        while j < len(b):
            result.append(b[j])
            j += 1
    elif j == len(b):
        while i < len(a):
            result.append(a[i])
            i += 1

    return result


def merge_sort(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return nums

    mid = int(len(nums) - 1 / 2)

    a = merge_sort(nums[0:mid])
    b = merge_sort(nums[mid:])

    return _sorted_sort(a, b)

def _partition(low, high, nums):
    if low >= high:
        return low, nums

    pivot = high
    i, j = low, pivot
    while i <= j:
        while nums[i] < pivot and i<=j:
            i += 1
        while nums[j] > pivot and i<=j:
            j -= 1
        else:
            nums[i], nums[j] == nums[j], nums[i]
            i += 1
            j -= 1
    if j != pivot:
        nums[pivot], nums[j] = nums[j], nums[pivot]
    return j, nums


def quick_sort(nums, low=None, high=None):
    if not low:
        low = 0
    if not high:
        high = len(nums) - 1
    if low >= high:
        return nums

    idx, nums = _partition(low, high, nums)

    if idx - 1 <= high:
        quick_sort(nums, low, idx - 1)
    quick_sort(nums, idx+1, high)

    return nums




def _partition(nums, low, high):
    diff = high - low
    if diff == 0:
        return None, nums

    i, j, pivot = low, high - 1, high
    while True:
        while nums[i] < nums[pivot] and i <= j and i < pivot:
            i += 1
        while nums[j] > nums[pivot] and i <= j and j >= low:
            j -= 1
        if i > j or j < low or i >= pivot:
            break
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    if i != pivot:
        nums[i], nums[pivot] = nums[pivot], nums[i]

    return i, nums

def quick_sort(nums, low = 0, high = None):
    if high is None:
        high = len(nums) - 1
    if low < 0 or high >= len(nums) or low >= high:
        return nums

    idx, nums = _partition(nums, low, high)

    if idx is not None:
        nums = quick_sort(nums, low, idx - 1)
        nums = quick_sort(nums, idx + 1, high)

    return nums


data = [
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ([1, 3, 2, 4], [1, 2, 3, 4]),
    ([1, 4, 2, 3], [1, 2, 3, 4]),
    ([1, 3, 3, 1], [1, 1, 3, 3]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([1, 3, 2, 6, 1], [1, 1, 2, 3, 6])
]

@pytest.mark.parametrize("inp, out", data.copy())
def test_selection_sort(inp, out):
    assert selection_sort(inp) == out

@pytest.mark.parametrize("inp, out", data.copy())
def test_bubble_sort(inp, out):
    assert bubble_sort(inp) == out

@pytest.mark.parametrize("inp, out", data.copy())
def test_merge_sort(inp, out):
    assert merge_sort(inp) == out

@pytest.mark.parametrize("inp, out", data.copy())
def test_quick_sort(inp, out):
    assert quick_sort(inp) == out


@pytest.mark.parametrize("inp, out", data.copy())
def test_quick_sort(inp, out):
    assert quick_sort(inp) == out
