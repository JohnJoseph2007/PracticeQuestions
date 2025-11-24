from itertools import accumulate
from operator import not_

class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        return [*map(not_,accumulate(nums,lambda q,v:(q*2+v)%5))]
    
# map:
# first argument: not_ (negation function)
#   used to convert any zeros to True and non-zeroes to False
# second argument: accumulate(...)
#   generates the remainders of the binary numbers modulo 5
# accumulate:
#   first argument: nums (the input list of binary digits)
#   second argument: lambda q,v:(q*2+v)%5
#     q: the accumulated value (current remainder), serves as the exponent part during binary to decimal conversion
#     v: the current binary digit being processed
#     (q*2+v)%5: updates the accumulated value by shifting left (multiplying by 2) and adding the current digit, then taking modulo 5
# If divisible, the remainder is 0, which is False, which is converted to True by not_
# Works for very large inputs

# Not an easy question AT ALL
# Woah.
# Worth it though.