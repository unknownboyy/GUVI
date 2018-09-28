d=[]
def solve(m,n,i,mm):
    if m==0 and i>=n:    return 1
    if i<n or mm-m<i: return 0
    d=0
    for j in range(n,m+1):
        d=max(d,solve(m-j,n,j,mm))
    return d
for _ in range(int(input())):
    m,n=map(int,input().split())
    count=0
    for i in range(m,n-1,-1):
        count+=solve(m-i,n,i,m)
    print(count)