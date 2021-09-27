"""
https://www.geeksforgeeks.org/cutting-a-rod-dp-13/

Solution:
T[n] = min(
    V(n),
    V(n-1), T[1],
    V(n-2), T[2],
    V(n-3), T[3],
    ..
    V(1), T[n-1]
)
"""
def iter_solution(arr):
    result = [-1]*len(arr)

    for i, v in enumerate(arr):
        result[i] = v
        if i > 0:
            for j in range(i):
                result[i] = max(result[i], arr[j] + result[i-j-1])

    return result[-1]

def test_iter_solution():
    # assert iter_solution([1, 2, 5]) == 5
    assert iter_solution([1, 5, 8, 9, 10, 17, 17, 20]) == 22






