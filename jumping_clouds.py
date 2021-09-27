"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

variables:
jumps
if step += 2 is 0, then jemp
else step += 1 and jump
"""

def jumpingOnClouds(c):
    i, total, jump = 0, len(c), 0
    if total in [0, 1]:
        return total
    while i < total - 1:
        if i == total - 1:
            jump += 1
            break
        else:
            if c[i+2] == 0:
                jump += 1
                i += 2
            else:
                jump += 1
                i += 1
    return jump


def test_func():
    assert jumpingOnClouds([0, 0, 0, 0, 1, 0]) == 3


