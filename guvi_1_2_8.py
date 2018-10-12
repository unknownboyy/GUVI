def isarmstrong(n):
    count=0
    for i in str(n):
        count+=int(i)**3
    if n==count:
        return True
    else:
        return False
n,m=map(int,input().split())
for i in range(n+1,m):
    if isarmstrong(i):
        print(i,end=' ')