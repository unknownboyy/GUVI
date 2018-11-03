def solve(s,n):
    i=0
    while i<n and s[i]=='#':
        i+=1
    ind=i
    for i in range(ind,n-1):
        if s[i]=='#' and s[i+1]=='#':
            return False
    q=s[ind:].count('#')
    count=0
    while ind<n and q>0:
        if s[ind]=='.':
            count+=q
        else:
            q-=1
        ind+=1
    return count
for _ in range(int(input())):
    n=int(input())
    s=list(input())
    x=solve(s,n)
    if x:
        print(x)
    else:
        print(-1)