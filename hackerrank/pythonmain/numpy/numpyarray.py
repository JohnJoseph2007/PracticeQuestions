# Link: https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = arr[::-1]
    return numpy.array(arr, float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
