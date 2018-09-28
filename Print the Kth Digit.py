for _ in range(int(input())) :
    a,b,k=map(int,input().split())
    y=pow(a,b,10**(k))
    print(str(y)[0]) if len(str(y))==k else print(0)