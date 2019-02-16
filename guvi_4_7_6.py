try:
    a,b,f,k=map(int,input().split())
    if b<a:
        raise EnvironmentError
    if b>=2*a:
        print(k//2)
    elif b>2*a-f:
        print(k-1)
    elif b>=a:
        print(k)
    else:
        print(-1)
except:
    print('Invalid Input')