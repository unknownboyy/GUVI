for _ in range(int(input())) :
    m,n=map(int,input().split())
    m+=1;n+=1
    c=[0]*n
    c[0]=1
    for i in range(m):
        for j in range(1,n):
            c[i]+=c[i-1]
    print(c[n-1])