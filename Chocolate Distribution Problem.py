for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()));s.sort()
    m=int(input())
    mm=10**6+1
    for i in range(n-m+1):
        mm=min(mm,s[i+m-1]-s[i])
    print(mm)