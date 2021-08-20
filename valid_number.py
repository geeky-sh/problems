from typing import Pattern
import pytest
import re

class Solution:
    def isNumber(self, s: str) -> bool:
        """
        patterns:
        decimal
        integer
        with e
        """
        seen_sign, seen_digit, seen_exponent, seen_dot = False, False, False, False
        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
            elif ch in ('-', '+'):
                if i > 0 and s[i-1] not in ["e", "E"]:
                    return False
                seen_sign = True
            elif ch == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif ch in ["e", "E"]:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            else:
                return False
        return seen_digit






data = [
    ("2", True),
    ("0089", True),
    ("-0.1", True),
    ("+3.14", True),
    ("4.", True),
    ("-.9", True),
    ("2e10", True),
    ("-90E3", True),
    ("3e+7", True),
    ("+6e-1", True),
    ("53.5e93", True),
    ("-123.456e789", True),
    ("abc", False),
    ("1a", False),
    ("1e", False),
    ("e3", False),
    ("99e2.5", False),
    ("--6", False),
    ("-+3", False),
    ("95a54e53", False),
    ("+-", False)
]
@pytest.mark.parametrize("inp, out", data.copy())
def test_valid_number(inp, out):
    assert Solution().isNumber(inp) == out
