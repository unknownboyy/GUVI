for _ in range(int(input())) :
    n,m=map(int,input().split())
    s=input()
    if n>=m:    print(n*m)
    else:
        print(n**2)