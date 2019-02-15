for _ in range(int(input())):
    m,n=map(int,input().split())
    i=1
    while 2**i<n:
        i+=1
    print(i)