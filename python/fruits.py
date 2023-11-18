#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'foo' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY codeList
#  2. STRING_ARRAY shoppingCart
#

def findCode(code, shoppingCart, started=False):
    if not code:
        return True, shoppingCart
    if not shoppingCart:
        return False, shoppingCart
    item, remaining = code[0], code[1:]
    cartItem, remainingCart = shoppingCart[0], shoppingCart[1:]
    if item == 'anything' or item == cartItem:
        return findCode(remaining, remainingCart, True)
    elif started:
        return False, shoppingCart
    else:
        return findCode(code, remainingCart, started)



def foo(codeList, shoppingCart):
    if not codeList:
        return 1
    if not shoppingCart:
        return 0

    code = codeList[0]
    remainingCode = codeList[1:]

    isPresent, remainingCart = findCode(code, shoppingCart)
    if not isPresent:
        return 0
    else:
        return foo(remainingCode, remainingCart)

if __name__ == '__main__':
    assert foo([['o'], ['a', 'a'], ['b', 'o', 'a'], ['b']], ['o', 'a', 'a', 'b', 'o', 'a', 'b']) == 0