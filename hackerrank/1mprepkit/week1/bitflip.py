# Link-: https://www.hackerrank.com/challenges/one-month-preparation-kit-flipping-bits/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# You will be given a list of 32 bit unsigned integers. Flip all the bits ( and ) and return the result as an unsigned integer.

# Example:
# n = 9₁₀
# 9₁₀ = 1001₂
# We're working with 32 bits, so:
# 00000000000000000000000000001001₂ = 9₁₀
# 11111111111111111111111111110110₂ = 4294967286₁₀
# Return 4294967286

# Function Description:
# Complete the flippingBits function in the editor below.
# flippingBits has the following parameter(s):
#   - int n: an integer

# Returns:
#   - int: the unsigned decimal integer result

# Input Format:
# The first line of the input contains q, the number of queries.
# Each of the next q lines contain an integer, n, to process.

# Constraints:
# 1 <= q <= 100
# 0 <= n <= 2³²

# Sample Input:
# 3 
# 2147483647 
# 1 
# 0

# Sample Output:
# 2147483648 
# 4294967294 
# 4294967295

# Explanation:
# Take 1 for example,
# as unsigned 32-bits is 00000000000000000000000000000001,
# doing the flipping we get 11111111111111111111111111111110 which in turn is 4294967294

## CODE HERE :

import math
import os
import random
import re
import sys

def flippingBits(n):
    string = '{:032b}'.format(n)
    final = ""
    dummy = 0
    for i in string:
        if i=="0":
            dummy="1"
            final+=dummy
        elif i=="1":
            dummy="0"
            final+=dummy
    finaltoint = int(final, 2)
    print(finaltoint)



q = int(input().strip())
for _ in range(q):
    n = int(input().strip())
    result = flippingBits(n)

# Status: Finished