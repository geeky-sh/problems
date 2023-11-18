"""
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

variables required:
- count
- level

logic:
for each step:
    if step is U:
        level += 1
        if level == 0:
            count += 1
    else:
        level -= 1
"""

def countingValleys(steps, path):
    count, level = 0, 0
    for step in path:
        if step == 'U':
            level += 1
            if level == 0:
                count += 1
        else:
            level -= 1
    return count

def test_func():
    assert countingValleys(8, "UDDDUDUU") == 1