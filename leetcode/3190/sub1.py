class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ops = 0
        for i in nums:
            if i%3==0:
                ops+=0
            else:
                ops+=1
        return ops
    
# Easy, quick to code
# Figured out that for any number you only need at most 1 operation to make it divisible by 3.
