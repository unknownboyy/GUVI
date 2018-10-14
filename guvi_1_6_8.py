n,k=map(int,input().split())
s=list(map(int,input().split()))
counts=False
for i in s:
    if i==k:
        counts=True
print('yes') if counts else print('no')