from _pytest.capture import DontReadFromInput
import pytest
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        total_dominoes = len(dominoes)
        successful_pass = False
        while not successful_pass:
            successful_pass = True
            prev, nxt = None, None
            for idx, dominoe in enumerate(dominoes):
                nxt = dominoes[idx + 1] if idx < (total_dominoes - 1) else None
                if dominoe == ".":
                    if prev == "R" and nxt != "L":
                        successful_pass = False
                        dominoes[idx] = "R"
                    elif nxt == "L" and prev != "R":
                        successful_pass = False
                        dominoes[idx] = "L"
                prev = dominoe
        return "".join(dominoes)





data = [
    ("RR.L", "RR.L"),
    (".L.R...LR..L..", "LL.RR.LLRRLL..")
]

@pytest.mark.parametrize("inp, out", data.copy())
def test_dominoes(inp, out):
    assert Solution().pushDominoes(inp) == out