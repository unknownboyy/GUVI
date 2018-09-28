t=int(input())
for _ in range(t) :
    n=int(input())
    s=list(map(int,input().split()))
    c=[0]*(2*n)
    i=1
    su=sum(s)
    c[su-1]=1
    left=0;right=0
    i=0
    while i<n and s[i]!=1:
        su-=s[i]
        try:
            c[su-1]=1
        except:
            print(su-1)
        left+=s[i]
        i+=1
    su=sum(s)
    j=n-1
    while j>=0 and s[j]!=1:
        su-=s[j]
        try:
            c[su-1]=1
        except:
            print(su-1)
        right+=s[j]
        j-=1
    su=sum(s)
    tp=0
    for k in range(n):
        tp+=s[k]
        c[tp-1]=1
    tp=0
    for k in range(n-1,-1,-1):
        tp+=s[k]
        c[tp-1]=1
    
    print(sum(c[:2*n]))