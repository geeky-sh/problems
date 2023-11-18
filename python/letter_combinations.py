import pytest
from typing import List


class Solution:
    LETTER_MAP = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(self.LETTER_MAP[digits])
        else:
            firsts = list(self.LETTER_MAP[digits[0]])
            seconds = self.letterCombinations(digits[1:])
            result = []
            for s in seconds:
                for f in firsts:
                    result.append("{}{}".format(f, s))
            return result


data = [
    # ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
    ("", []),
    ("2", ["a", "b", "c"])
]

@pytest.mark.parametrize("inp, out", data.copy())
def test_solution(inp, out):
    assert Solution().letterCombinations(inp) == out

