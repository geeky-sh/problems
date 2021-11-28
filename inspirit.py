def _sumOfTheDigits(num):
    snum = str(num)
    res = ""
    count, pn = 0, ""
    for i, c in enumerate(snum):
        if i == 0:
            count, pn = 1, c
        elif pn != c:
            res += "{}{}".format(count, pn)
            count, pn = 1, c
        else:
            count += 1
    res += "{}{}".format(count, pn)
    return res

def sumOfTheDigits(q):
    res = []
    for num in q:
        res.append(_sumOfTheDigits(num))
    return res
