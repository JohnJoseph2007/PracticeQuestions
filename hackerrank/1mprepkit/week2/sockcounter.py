# Link: https://www.hackerrank.com/challenges/one-month-preparation-kit-sock-merchant/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    x = Counter(ar)
    c=0
    for i in x:
        if x[i]==2:
            c+=1
        elif x[i]>2:
            c+=(x[i]//2)
    return c
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
