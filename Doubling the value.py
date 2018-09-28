for _ in range(int(input())) :
    n,b=map(int,input().split())
    s=list(map(int,input().split()))
    for i in range(n):
        if s[i]==b:
            b*=2
    print(b)