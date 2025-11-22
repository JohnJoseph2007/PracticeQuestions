class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ops = 0
        for i in nums:
            ops+= min(i%3, 3-(i%3))
        return ops
    
# Also works, but requires more time and marginally less space.
# Cool solution, but overall not worth it.
        