for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    print(n-sum(s))