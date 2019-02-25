t = int(input())
for _ in range(t):
    n , k = map(int,input().split())
    m = 0
    options = []
    for i in range(n):
        l,r=map(int,input().split())
        options.append([l,r])
        m = max(m,l,r)
    m+=2
    c = [0]*(m)
    for i in options:
        c[i[0]]+=1
        c[i[1]+1]-=1
    x = 0
    w = []
    for i in range(m):
        x+=c[i]
        w.append(x)
    c1 = [0]*(m)
    c2 = [0]*(m)
    for i in range(1,m):
        if w[i]==k:
            c1[i]=1+c1[i-1]
        else:
            c1[i]=c1[i-1]
    d1 = [0]*(m)
    for i in range(1,m):
        if w[i]==k+1:
            d1[i]=1+d1[i-1]
        else:
            d1[i]=d1[i-1]
    for i in range(m-2,0,-1):
        if w[i]==k:
            c2[i]=1+c2[i+1]
        else:
            c2[i]=c2[i+1]
    mymax = 0
    for i in options:
        mymax = max(mymax,c1[i[0]-1]+c2[i[1]+1]+d1[i[1]]-d1[i[0]-1])
    print(mymax)