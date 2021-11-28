import pytest
from collections import defaultdict
from typing import List

class Solution:
    def get_box_index(self, i, j):
        if   0 <= i <= 2 and 0 <= j <= 2:
            return 0
        elif 0 <= i <= 2 and 3 <= j <= 5:
            return 1
        elif 0 <= i <= 2 and 6 <= j <= 8:
            return 2
        elif 3 <= i <= 5 and 0 <= j <= 2:
            return 3
        elif 3 <= i <= 5 and 3 <= j <= 5:
            return 4
        elif 3 <= i <= 5 and 6 <= j <= 8:
            return 5
        elif 6 <= i <= 8 and 0 <= j <= 2:
            return 6
        elif 6 <= i <= 8 and 3 <= j <= 5:
            return 7
        elif 6 <= i <= 8 and 6 <= j <= 8:
            return 8


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_cache = [defaultdict(lambda: 0)]*9
        cols_cache = [defaultdict(lambda: 0)]*9
        subboxes_cache = [defaultdict(lambda: 0)]*9
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                rcache = rows_cache[i][val]
                if rcache > 0:
                    import ipdb; ipdb.set_trace()
                    return False
                rcache += 1

                ccache = cols_cache[j][val]
                if ccache > 0:
                    import ipdb; ipdb.set_trace()
                    return False
                ccache += 1

                subi = self.get_box_index(i, j)
                if subboxes_cache[subi][val] > 0:
                    import ipdb; ipdb.set_trace()
                    return False
                subboxes_cache[subi][val] += 1

        return True

inp = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
def test_func():
    assert Solution().isValidSudoku(inp) == True



