size = int(input())
ratings = list(map(int, input().split()))

candies = ratings.copy()
for i in range(0, size):
    # candies[i] = 1
    # #backcheck
    # if ratings[i-1] > ratings[i]:
    #     candies[i-1]+=1
    #     break
    # elif ratings[i] > ratings[i-1]:
    #     candies[i]+=1
    #     break
    # #frontcheck
    # if ratings[i] > ratings[i+1]:
    #     candies[i]+=1
    # elif ratings[i+1] > ratings[i]:
    #     candies[i+1]+=1
    candies[i] = 1

for i in range(1, size):
    if ratings[i-1]>ratings[i]:
        candies[i-1]=candies[i]+1
    elif ratings[i]>ratings[i-1]:
        candies[i]=candies[i-1]+1
print(sum(candies))

# Partially correct solution, fails for some test cases