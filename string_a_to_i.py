import math
from typing import Pattern
import pytest
import re

class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Find the number_list and store it in an array
        Convert that number into an integer
        """
        pattern = "\s*([\-\+]{0,1}\d+).*"
        match = re.match(pattern, s)
        if not match:
            return 0

        number = int(match.groups()[0])
        low, high =  int(-math.pow(2, 31)), int(math.pow(2, 31) - 1)
        if number > high:
            return high
        if number < low:
            return low

        return number


data = [
    ("42", 42),
    ("-42", -42),
    ("  -42", -42),
    ("hello -5423", 0),
    ("hello - 5423", 0),
    ("  - 5423 hwllo", 0),
    ("-91283472332", -2147483648),
    ("+1", 1),
    ("+-12", 0)
]

@pytest.mark.parametrize("inp, out", data.copy())
def test_atoi(inp, out):
    assert Solution().myAtoi(inp) == out