n,m=map(int,input().split())
f=[True]*(m+1)
for i in range(2,m):
    if f[i]:
        for j in range(i+i,m,i):
            f[j]=False
for i in range(n+1,m):
    if f[i]:
        print(i,end=' ')