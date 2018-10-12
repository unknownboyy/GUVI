n,m=map(int,input().split())
if n%2==1:
    n+=1
else:
    n+=2
for i in range(n,m,2):
    print(i,end=' ')