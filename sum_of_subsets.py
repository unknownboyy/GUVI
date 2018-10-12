def getSubsetSums(s,n):
    li=[]
    size=2**n
    for i in range(size):
        su=0
        for j in range(n):
            if i & (1<<j):
                su+=s[j]
        li.append(su)
    return sorted(li)
for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    print(*getSubsetSums(s,n))