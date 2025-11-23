class Solution:
    def maxSumDivThree(self, nums: list[int]):
        total = 0
        sone = float("inf")
        stwo = float("inf")
        for i in nums:
            total += i
            if i%3==1:
                stwo = min(stwo, i+sone)
                sone = min(sone, i)
            if i%3==2:
                sone = min(sone, i+stwo)
                stwo = min(stwo, i)
        sone = int(sone)
        stwo = int(stwo)
        if total%3==0:
            return total
        if total%3==1:
            return total-sone
        if total%3==2:
            return total-stwo

# I don't understand this.
# At. ALL.
# I need to figure it out soon, and I will.
# I used NeetCodeIO's video as reference to grasp the concept.
# https://www.youtube.com/watch?v=F6hHAdknock