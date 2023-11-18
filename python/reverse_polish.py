import pytest

def compute_reverse_polish_notation(arr, result=None):
    if not arr and not result:
        return None
    if not arr:
        return result[0]

    if result is None:
        result = []

    item = arr[0]
    rem = arr[1:]
    if item.isdigit():
        result.append(int(item))
    if item in ['+', '-', '*', '/']:
        a = result.pop()
        b = result.pop()
        if item == '+':
            result.append(a+b)
        if item == '*':
            result.append(a*b)
        if item == "/":
            result.append(int(a/b))
        if item == '-':
            result.append(a-b)

    return compute_reverse_polish_notation(rem, result)

def test_reverse_polish():
    assert compute_reverse_polish_notation(["2", "1", "+", "3", "*"]) == 9