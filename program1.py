t=int(input())
for _ in range(t) :
    n=int(input())
    s=list(map(int,input().split()))
    c=[0]*(n)
    for i in s:
        if i<=n:
            c[i-1]+=1
    count=0
    for i in range(n):
        if c[i]==0:
            count+=1
    print(count)