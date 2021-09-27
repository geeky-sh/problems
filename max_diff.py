"""
https://www.interviewbit.com/problems/maximum-absolute-difference/
"""

import math
class Solution:
    # @param A : list of integers
    # @return an integer

    def maxArr(self, A):

        result = 0
        max_i = math.ceil(len(A) / 2)
        for i in range(0, len(A)):
            for j in range(i + 1, len(A)):
                r = abs(A[i] - A[j]) + abs(i - j)
                if r == 84:
                    print(i, j, len(A), r)
                result = max(result, r)

        return result

def test_func():
    # assert Solution().maxArr([ 49, -24, -49, 56, -26, 78, 25, -100, -73, 31 ]) == 180
    assert Solution().maxArr([ 81, 73, 53, 64, 90, 23, 66, 12, 66, 94 ]) == 84