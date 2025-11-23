class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candies[i] = candies[i-1]+1
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)

        return sum(candies)

# Two pass solution
# Two passes are required, to ensure both left and right neighbor rules stay valid.
