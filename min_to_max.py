for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    q = int(input())
    li = list(map(int,input().split()))
    ri = list(map(int,input().split()))
    x = list(map(int,input().split()))
    p = int(input())
    s = []
    for i in range(q):
        s.append([li[i],ri[i],x[i],x[i]*(ri[i]-li[i]+1)])
    s.sort(key=lambda x:x[3])
    c = [0]*(n+1)
    for i in range(p):
        l,r,val,ww = s[i]
        c[l]+=val
        c[r+1]-=val
    c1 = []
    val = 0
    for i in range(len(c)):
        val+=c[i]
        c[i]=val
    for i in range(n):
        c1.append(c[i]+arr[i])
    
    s.sort(key=lambda x:x[3],reverse=True)
    c = [0]*(n+1)
    for i in range(p):
        l,r,val,ww = s[i]
        c[l]+=val
        c[r+1]-=val
    c2 = []
    val = 0
    for i in range(len(c)):
        val+=c[i]
        c[i]=val
    for i in range(n):
        c2.append(c[i]+arr[i])
    m = 10**9+7
    print(sum(c2)%m,sum(c1)%m)