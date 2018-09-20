for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    i=0;j=0
    c=[0]*(n+1)
    while i<n and j<n:
        while i<n and s[i]%2==1:
            i+=1
        if i<n: print(s[i],end=' ');c[i]=1
        i+=1
        while j<n and s[j]%2==0:
            j+=1
        if j<n: print(s[j],end=' ');c[j]=1
        j+=1
    while i<n:
        if c[i]==0:
            print(s[i],end=' ');c[i]=1
        i+=1
    while j<n:
        if c[j]==0:
            print(s[j],end=' ');c[j]=1
    print('')