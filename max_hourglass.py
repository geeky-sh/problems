def hourglassSum(arr):
    lrows = len(arr)
    lcols = len(arr[0])

    result = None
    for i in range(lrows - 2):
        for j in range(lcols - 2):
            tresult = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            tresult += arr[i+1][j+1]
            tresult += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if not result:
            result = tresult
        else:
            result = max(result, tresult)
    return result