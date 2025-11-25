class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0

        for i in range(1,k+1):
            remainder = (remainder*10+1)%k
            if remainder == 0:
                return i
        return -1
    
# Remainder is used to avoid very large numbers.
# The loop runs at most k times because of the pigeonhole principle.
# If we don't find a "repunit" divisible by k within k iterations, it means
# that the remainders have started to repeat, indicating no such "repunit" exists.

# A number 'k' has exactly k numbers before it (from 0)
# So if we have more than k remainders, at least two of them must be the same.
# This is the pigeonhole principle.
