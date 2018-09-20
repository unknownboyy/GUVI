def solve(s):
    c=[0]*(10**3+1)
    for i in s:
        c[i]+=1
    area=-1;sqcount=-1
    for i in range(10**3+1):
        if c[i]>3 and area<i*i:
            sqcount=c[i]//4
            area=i*i
    if sqcount==-1: print(-1)
    else:
        print(area,sqcount)
for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    solve(s)