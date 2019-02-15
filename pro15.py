n,m,k=map(int,input().split())
shops = [0]*n
for _ in range(n):
    s = list(map(int,input().split()))
    for i in range(1,s[0]):
        shops[s[0]-1]^=s[i]
uvlist = []
for _ in range(m):
    uvlist.append(list(map(int,input().split())))
