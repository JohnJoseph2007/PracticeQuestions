# Link: https://www.hackerrank.com/challenges/one-month-preparation-kit-angry-children/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    x = sorted(arr)
    minu = max(x)-min(x)
    xdash = []
    for i in range(0, len(x)-k):
        if x[i+k-1]-x[i] <=minu:
            xdash = x[i:k]
            minu = x[k-1]-x[i]
        else:
            return minu
    return (max(xdash)-min(xdash))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
