n,k=map(int,input().split())
s=list(map(int,input().split()))
ss=[]
for i in s:
    if i%2==1:
        ss.append(i)
print(ss[k-1])