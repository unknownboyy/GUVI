<<<<<<< HEAD
# LRU
n = int(input())
l = []
lsize = int(input())
s = list(map(int,input().splti()))
count=0
for i in s:
    if i in l:
        l.remove(i)
        l.append(i)
    else:
        l.append(i)
        if len(l)>lsize:
            l.pop(0)
        count+=1
print(count)
=======
for _ in range(int(input())) :
    n,m,k,l=map(int,input().split())
    s=list(map(int,input().split()))
    s.sort()
    wait=10**15+1
    for i in range(n):
        if s[i]<=k:
            wait=min(wait,(m+i+1)*l-s[i])
    print(min(wait,(m+n+1)*l-k)) 
>>>>>>> 33f4cd762d4e4b8b825025741676af85251a142b
