n=int(input())
s=list(map(int,input().split()))
d=dict()
maxx=0;occur=0
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    if occur<d[i]:
        occur=d[i]
        maxx=i
    elif occur==d[i]:
        maxx=min(maxx,i)
print(maxx)