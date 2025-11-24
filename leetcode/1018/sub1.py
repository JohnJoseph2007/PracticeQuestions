import sys
class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        sys.set_int_max_str_digits(0)
        x = 0
        b = []
        for i in nums:
            x *= 10
            x += i
            t = int(str(x), 2)
            print(t)
            if t%5==0:
                b.append(True)
            else:
                b.append(False)
        return b

# Works for smaller inputs but fails for very large inputs
# Thought of this in 20 mins
# Thought about it for a while
# Realised something, check next submission.