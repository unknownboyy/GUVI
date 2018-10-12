for _ in range(int(input())) :
    a,b,k=map(int,input().split())
    if ((a+b)//k)%2==0:
        print('CHEF')
    else:
        print('COOK')