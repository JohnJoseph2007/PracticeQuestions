# Link: https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true

import numpy
s = input().split()
x = list(map(int, s))
print(numpy.reshape(x, (3,3)))
