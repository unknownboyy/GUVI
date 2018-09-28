for _ in  range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    c=[0]*21
    for i in s:
        c[i]+=1
    su=0
    for i in range(20,0,-1):
        if c[i]>0:
            su+=c[i]*i
            c[i-1]-=c[i]
            if c[i-1]<0:
                c[i-1]=0
    print(su)