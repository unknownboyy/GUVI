def dist(src,dest):
    return ((src[0]-dest[0])**2+(src[1]-dest[1])**2)**0.5
def radius(src,index,s):
    r = 10**9+7
    for i in range(len(s)):
        if i!=index:
            r = min(r,dist(src,s[i]))
    return r
for _ in range(int(input())):
    t = int(input())
    s=[]
    for i in range(t):
        s.append(list(map(int,input().split())))
    rad = []
    for i in range(t):
        rad.append(radius(s[i],i,s))
    for i in range(t):
        count = 0
        for j in range(t):
            if dist(s[i],s[j])<=2*rad[i]:
                count+=1
        print(("%.2f"%(rad[i])),count-1)