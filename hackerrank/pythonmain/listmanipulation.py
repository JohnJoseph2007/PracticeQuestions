# Link: https://www.hackerrank.com/challenges/python-lists/problem

def ex(l, retlist):
    x = l.split()
    if x[0]=="insert":
        retlist.insert(int(x[1]),int(x[2]))
    elif x[0]=="print":
        print(retlist)
    elif x[0]=="remove":
        if int(x[1]) in retlist:
            retlist.remove(int(x[1]))
    elif x[0]=="append":
        retlist.append(int(x[1]))
    elif x[0]=="sort":
        retlist.sort()
    elif x[0]=="pop":
        retlist.pop()
    elif x[0]=="reverse":
        retlist.reverse()
        
if __name__ == '__main__':
    n = int(input())
    push = []
    for i in range(n):
        ex(input(), push)
    
