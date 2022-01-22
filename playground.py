## TEST CODE HERE :

import math
import os
import random
import re
import sys

def staircase(n):
    space = " "
    hashsign = "#"
    index = 0
    spaces = 6
    array = []
    # Write your code here
    for i in range(1, n+1):
        spaces-=i
        #for i in range(spaces):
        array.append(space)
        print(array)
        array = []
        spaces = 6

n = int(input().strip())
print("-------------------------------------------------------------------")
staircase(n)


# Ignore the initial hashes. This is the final output if n = 6. Also ignore the box.
#      |      # |
#      |     ## |
#      |    ### |
#      |   #### |
#      |  ##### |
#      | ###### |