# Link: https://www.hackerrank.com/challenges/one-month-preparation-kit-caesar-cipher-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    k=k%26
    al = string.ascii_lowercase
    sal = al[k:]+al[:k]
    encrypt = ""
    for i in s:
        if i.isalpha():
            if i.isupper():
                x = al.index(i.lower())
                encrypt = encrypt + sal[x].upper()
            else:
                x = al.index(i)
                encrypt = encrypt + sal[x]
        else:
            encrypt = encrypt + i
    return encrypt
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
