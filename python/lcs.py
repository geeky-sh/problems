"""
https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
"""
import pytest

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lt1 = len(text1)
        lt2 = len(text2)

        result = []
        for _x in range(0, lt1):
            result.append([0]*lt2)

        for i in range(0, lt1):
            for j in range(0, lt2):
                m1, m2, m3 = 0, 0, 0
                if j > 0:
                    m3 = result[i][j-1]
                if i > 0:
                    m2 = result[i-1][j]

                if text1[i] == text2[j]:
                    m1 += 1
                if i > 0 and j > 0:
                    m1 += result[i-1][j-1]

                result[i][j] = max(m1, m2, m3)

        return result[i][j]


data = [
    ("ABCDGH", "AEDFHR", 3),
]

@pytest.mark.parametrize("t1, t2, out", data.copy())
def test_lcs(t1, t2, out):
    assert Solution().longestCommonSubsequence(t1, t2) == out