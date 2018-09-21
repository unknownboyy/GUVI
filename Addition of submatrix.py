for _ in range(int(input())) :
    m,n=map(int,input().split())
    s=list(map(int,input().split()))
    x1,y1,x2,y2=map(int,input().split())
    mysum=0
    for i in range(x2-x1+1):
        for j in range(y2-y1+1):
            mysum+=s[(x1+i-1)*n+y1+j-1]
    print(mysum)