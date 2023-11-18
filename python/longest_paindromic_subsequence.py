"""
Problem:
https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
"""
import pytest


def longest_palindromic_subsequence(A):
    length = len(A)

    result = []
    for _x in A:
        result.append([0]*length)

    for i in range(length):
        for j in range(length):
            m, n1, n2, n = 0, 0, 0, 0

            if m > 0 and A[i] == A[j]:
                m = 2 + result[i-1][j-1]

            if i > 0:
                n1 = result[i-1][j]
            if j > 0:
                n2 = result[i][j-1]

            n = max(n1, n2)
            result[i][j] = max(m, n)

    return result[i][j]


def test_func():
    assert longest_palindromic_subsequence('geeksforgeeks') == 5