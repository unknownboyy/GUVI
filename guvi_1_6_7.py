n,k=map(int,input().split())
s=list(map(int,input().split()))
counts=0
for i in s:
    if i==k:
        counts+=1
print(counts)