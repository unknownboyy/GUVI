try:
    n,k=map(int,input().split())
    if k*2<=n:
        print(1,k)
    elif k>n:
        print(-1)
    else:
        print(1,n-k)
except:
    print('Invalid Input')