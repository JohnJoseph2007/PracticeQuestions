n1 = int(input())
a1 = list(map(int, input().split()))
n2 = int(input())
a2 = list(map(int, input().split()))
ans = ""
a3 = sorted(a1+a2)
if (n1+n2)%2==0:
    x1 = a3[(n1+n2)//2]
    x2 = a3[((n1+n2)//2)-1]
    ans = str(float((x1+x2)/2))
else:
    x1 = a3[(n1+n2)//2]
    ans = str(float(x1))
    
print(ans+"0"*(6-len(ans[ans.index("."):])))