def powfunc(num):
    result = 0
    result = num * num
    return result

def getMax(int1, int2):
    if int1 >= int2:
        maxVal = int1
    else:
        maxVal = int2
    return maxVal

def getMin(int1, int2):
    if int1 <= int2:
        minVal = int1
    else:
        minVal = int2
    return minVal

def power(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result