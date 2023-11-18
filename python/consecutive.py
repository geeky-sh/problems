def find_consecutive(nums, k):
    i = 0
    j = i + k - 1
    max_sum = sum(nums[0:j])
    while i < len(nums-k):
        current_sum = current_sum - nums[i] + nums[j]
        max_sum = max(current_sum, max_sum)
        i += 1
        j += 1
    return max_sum

def max_zeros_by_flipping_subarray(bary):
    zero_count, first, size, max_ones = 0, 0, 0, 0
    for i, v in enumerate(bary):
        if v == 1 and first + size == i:
            size += 1
        elif v == 1:
            first = i
            size = 1
        else:
            zero_count += 1
        max_ones = max(max_ones, size)
    return zero_count + max_ones