from collections import deque
from functools import reduce
import operator
from typing import List

def _re_compute_expr(tokens: List, values: List = None):
    if values is None:
        values = []
    if not tokens:
        return values[0]
    token = tokens[0]
    remaining = tokens[1:]
    if token.isdigit():
        values.append(int(token))
    elif token in ["+", "*"]:
        values.append(token)
    elif token == "(":
        pass
    elif token == ")":
        operands = []
        v = values.pop()
        while isinstance(v, int):
            operands.append(v)
            v = values.pop()
        op = v
        if op == "+":
            values.append(sum(operands))
        elif op == "*":
            values.append(reduce(operator.mul, operands))
    return _re_compute_expr(remaining, values)




def re_compute_expr(exp):
    return _re_compute_expr(exp.split(" "))

def compute_expr(exp):
    tokens = exp.split(" ")
    if tokens[0].isdigit():
        return tokens[0]

    stack = deque([])
    for e in tokens:
        if e == "(":
            continue
        elif e == ")":
            elements = []
            x = stack.pop()
            while x not in ["+", "*"]:
                elements.append(x)
                x = stack.pop()
            op = x
            if op == "+":
                stack.append(sum(elements))
            elif op == "*":
                stack.append(reduce(operator.mul, elements))
        else:
            if e.isdigit():
                e = int(e)
            stack.append(e)

    return stack[0]



def test_eval():
    assert re_compute_expr("( + 7 ( * 8 12 ) )") == 103
    assert re_compute_expr("7") == 7