f=[0,1,1]
while f[-1]<=1009:
    f.append(f[-1]+f[-2])
for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    x=list(filter(lambda x:x in f,s))
    print(*x)