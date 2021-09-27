"""
https://www.interviewbit.com/problems/minimum-lights-to-activate/
"""

import builtins


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        """
        previous_bulb_position = -1
        start with bulb_position = B - 1
        if bulb_position == previous_bulb_position, then break
        check if right_lighted_area >= len(B) if yes break
        else new_bulb_position = bulb_position + 2*(B-1)
        """
        result= 0
        previous_bulb_position = -1
        bulb_position = min(len(A) - 1, B-1)
        if len(A) < 2*(B-1):
            return 1
        while True:
            if bulb_position == previous_bulb_position:
                return -1
            if A[bulb_position] == 0:
                bulb_position -= 1
            else:
                result += 1
                ext_lighted_area = bulb_position + B - 1
                if ext_lighted_area >= len(A) - 1:
                    return result
                else:
                    previous_bulb_position = bulb_position
                    bulb_position = min(
                        bulb_position + 2*(B-1) + 1,
                        len(A) - 1
                    )

def test_func():
    assert Solution().solve([ 0, 0, 1, 1, 1, 0, 0, 1], 3) == 2
    assert Solution().solve([ 0, 0, 0, 1, 0], 3) == -1




