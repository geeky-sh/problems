import math
from typing import Pattern
import pytest

class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Find the number_list and store it in an array
        Convert that number into an integer
        """
        number_list = []
        is_negative = None
        for ch in s:
            if number_list:
                if ch.isdigit():
                    number_list.append(int(ch))
                else:
                    break
            else:
                if ch.isspace():
                    if is_negative is not None:
                        break
                    else:
                        continue
                elif ch.isdigit():
                    number_list.append(int(ch))
                elif is_negative is None and ch == "-":
                    is_negative = True
                elif is_negative is None and ch == '+':
                    is_negative = False
                else:
                    break

        number_list.reverse()
        low, high, number =  int(-math.pow(2, 31)), int(math.pow(2, 31) - 1), 0
        for i, digit in enumerate(number_list):
            addr = math.pow(10, i) * digit
            if is_negative:
                addr = - addr
            if number + addr > high:
                return high
            elif number + addr < low:
                return low
            else:
                number += addr
        return int(number)




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