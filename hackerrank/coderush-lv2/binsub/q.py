size = int(input())
array = list(map(int, input().split()))
goal = int(input())

c = 0
for i in range(0, size):
    for j in range(i, size):
        # print(array[i:j+1])
        if sum(array[i:j+1])==goal:
            c+=1

print(c)
