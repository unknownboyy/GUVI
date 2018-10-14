myp=[True]*(10**5+1)
for i in range(2,int((10**5+1)**0.5)+1):
    if myp[i]:
        for j in range(i+i,10**5+1,i):
            myp[j]=False
l,r=map(int,input().split())
count=0
for i in range(l,r+1):
    if myp[i]:  count+=1
print(count)