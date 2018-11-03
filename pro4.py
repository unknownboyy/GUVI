from functools import reduce
for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    prod = reduce((lambda x,y:x*y),s)
    ss=s.copy()
    for i in range(n):
        ss[i]=prod//ss[i]
    print(*ss) 