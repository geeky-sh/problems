"""
https://leetcode.com/problems/partition-equal-subset-sum/
"""
from typing import List
import pytest

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        sum_nums = int(sum_nums / 2)

        result = []
        for _n in nums:
            result.append([0]*len(sum_nums))

        for i, num in enumerate(nums):
            for sum_no in range(sum_nums + 1):
                if sum_no == 0:
                    continue
                else:
                    m1, m2 = 0, 0
                    if i > 0:
                        m2 = result[i-1][sum_no]
                    if sum_no >= num:
                        if sum_no == num:
                            m1 = 1
                        m1 += result[i-1][sum_no-num]
                    result[i][sum_no] = m1 + m2

        return result[i][sum_no] == 2


data = [
    ([1, 5, 11, 5], True)
]

