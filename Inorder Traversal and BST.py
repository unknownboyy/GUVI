for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    flag=True
    for i in range(n-1):
        if s[i]>=s[i+1]:
            flag=False;break
    print(1) if flag else print(0)