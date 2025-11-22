size = int(input())
height = list(map(int, input().split()))

twod = []
for i in height:
    x = [1]*i+[0]*(size-i)
    twod.append(x)

c = 0
for i in range(0,len(twod)):
    y = []
    for j in range(0, len(twod)):
        y.append(twod[j][i])
    if 1 in y:
        for j in y:
            c+=y[y.index(1):(len(twod) - y[::-1].index(1))].count(0)

print(int(c/size))

