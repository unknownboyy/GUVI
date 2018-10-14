n=int(input())
s=list(map(int,input().split()))
d=dict()
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
mydict=[]
for i in d:
    if d[i]==1:
        mydict.append(i)
if len(mydict)==0:
    print('unique')
else:
    print(*sorted(mydict))