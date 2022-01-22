## TEST CODE HERE :

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max = 0
    maxarray = []
    # Write your code here
    for i in candles:
        if i>max:
            max = i
            maxarray = []
            maxarray.append(i)
        elif i==max:
            maxarray.append(i)
    print(len(maxarray))



candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
result = birthdayCakeCandles(candles)