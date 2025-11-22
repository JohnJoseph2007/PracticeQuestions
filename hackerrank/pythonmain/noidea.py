# Link: https://www.hackerrank.com/challenges/no-idea/problem

s1, s2 = map(int,input().split())
nums = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

happiness = 0
for i in nums:
    if i in a:
        happiness+=1
    elif i in b:
        happiness-=1

print(happiness)

# Whuh
# is
# going
# on