n = int(input())
arr = []
d = dict()
for _ in range(n):
    x,y=map(int,input().split())
    arr.append([x,y,x+y])
    w = x+y
    if w in d:
        d[w]+=1
    else:
        d[w]=1
count = 0
s = int(input())
for i in d:
    if i-s in d:
        count+=(d[i]*d[i-s])
print(count)