m,n=map(int,input().split())
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
d=dict()
for i in s1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
flag=True
for i in s2:
    if i not in d:
        flag=False
    else:
        d[i]-=1
for i in d:
    if d[i]<0:
        flag=False
print('YES') if flag else print('NO')