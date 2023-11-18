import pytest
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)

        if l in [0, 1]:
            return l

        result = [1] * l
        j, i = 0, 1
        for i in range(1, l):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    result[i] = max(result[i], 1+result[j])

        return max(result)


data = [
    ([10,9,2,5,3,7,101,18], 4),
    ([101, 102, 103, 104, 1, 2, 3, 4, 5], 5),
    ([0,1,0,3,2,3], 4)
]

@pytest.mark.parametrize("inp, out", data.copy())
def test_lis(inp, out):
    assert Solution().lengthOfLIS(inp) == out