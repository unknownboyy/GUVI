for i in range(int(input())):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    count=0
    for i in s:
        if i!=1:
            count+=1
    if count<=k:
        print('YES')
    else:
        print('NO') 