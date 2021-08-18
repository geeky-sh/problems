import pytest

class Solution:
    ROMAN_MAP = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    ROMAN_SUBTRACT_MAP = {
        "IV": 4, "IX": 9,
        "XL": 40, "XC": 90,
        "CD": 400, "CM": 900
    }
    def romanToInt(self, s: str) -> int:
        result, prev = 0, ""
        for x in s:
            two_fer = prev + x
            if two_fer in self.ROMAN_SUBTRACT_MAP:
                result = result - self.ROMAN_MAP[prev] + self.ROMAN_SUBTRACT_MAP[two_fer]
            else:
                result += self.ROMAN_MAP[x]
            prev = x
        return result

data = [
    ('III', 3),
    ('IV', 4),
    ("LVIII", 58),
    ("LIX", 59)
]

@pytest.mark.parametrize("inp, out", data.copy())
def test_solution(inp, out):
    assert  Solution().romanToInt(inp) == out

