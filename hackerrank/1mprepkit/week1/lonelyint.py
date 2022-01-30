# Link: https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one&h_r=next-challenge&h_v=zen

# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example:
# a = [1,2,3,4,3,2,1]
# The unique element is 4.

# Function Description:
# Complete the lonelyinteger function in the editor below.
# lonelyinteger has the following parameter(s):
# int a[n]: an array of integers

# Returns:
# int: the element that occurs only once

# Input Format:
# The first line contains a single integer, n, the number of integers in the array.
# The second line contains n space-separated integers that describe the values in a.

# Constraints:
# 1 <= n < 100
# It is guaranteed that n is an odd number and that there is one unique element.
# 0 <= a[i] <= 100, where 0 <= i < n.

## CODE HERE :

from collections import Counter
from operator import index

def lonelyinteger(a):
    # Write your code here
    data = Counter(a)
    e = list(data.values())
    f = list(data.items())
    index = e.index(min(e))
    num, k = f[index]
    print(num)

n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = lonelyinteger(a)

# Status: Finished