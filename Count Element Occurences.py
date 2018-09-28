for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    k=int(input())
    d=dict();count=0
    for i in s:
        if i in d:  d[i]+=1
        else:
            d[i]=1
    for i in d:
        if d[i]>n/k:
            count+=1
    print(count)