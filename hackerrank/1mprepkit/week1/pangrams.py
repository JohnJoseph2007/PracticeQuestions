# Link: https://www.hackerrank.com/challenges/one-month-preparation-kit-pangrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    lstring = "abcdefghijklmnopqrstuvwxyz"
    for i in s.lower():
        if i.isalpha() and (i in lstring):
            t= lstring.partition(i)
            lstring = t[0]+t[2]
    else:
        if len(lstring)==0:
            return "pangram"
        else:
            return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
