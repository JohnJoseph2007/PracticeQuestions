# Link: https://www.hackerrank.com/challenges/one-month-preparation-kit-two-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # Write your code here
    # A.sort()
    # B.sort()
    # B = B[::-1]
    # c, d = [], []
    # for i in range(len(A)):
    #     for j in range(len(B)):
    #         if (A[i]+B[j])>=k:
    #             c.append(A[i])
    #             d.append(B[i])
    #     else:
    #         if A==c and B==d:
    #             return "YES"
    #         else:
    #             return "NO"
    # summate = sum(A)+sum(B)
    # if summate>=k*(len(A)):
    #     return "YES"
    # else:
    #     return "NO"
    A = [x-k for x in A]
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        if A[i]+B[i]<0:
            return "NO"
    return "YES"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
