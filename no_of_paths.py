for _ in range(int(input())) :
    a,b=map(int,input().split())
    c=[[1 for i in range(a)] for i in range(b)]
    for i in range(1,b):
        for j in range(1,a):
            c[i][j]=c[i-1][j]+c[i][j-1]
    print(c[b-1][a-1])