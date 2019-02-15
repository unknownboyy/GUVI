def getMinCostNode(cost,visited):
    myCost=10**6+2;node=-1
    for i in range(len(visited)):
        if visited[i]==False and cost[i]<myCost:
            myCost=cost[i]
            node=i
    return node
def doDijksatra(s,k,n):
    visited=[False]*n
    cost=[10**6+1]*n
    cost[k]=0
    q=n
    while q>0:
        app=getMinCostNode(cost,visited)
        visited[app]=True
        for i in s[app]:
            cost[i[0]]=min(cost[i[0]],cost[app]+i[1])
        q-=1
    return cost

n,m=map(int,input().split())
c=[[1000000 for x in range(n)] for x in range(n)]
edges = []
true_false = []
for i in range(m):
    a,b,s=map(int,input().split())
    edges.append([a,b,s])
    c[a-1][b-1]=min(c[a-1][b-1],s)
    c[b-1][a-1]=min(c[a-1][b-1],s)
s=[[] for j in range(n)]
for i in range(n):
    for j in range(i+1,n):
        if c[i][j]!=1000000:
            s[i].append([j,c[i][j]])
            s[j].append([i,c[i][j]])
k=n
myarr=doDijksatra(s,k-1,n)
cost = myarr
for i in range(n):
    if myarr[i]==10**6+1:
        myarr[i]=-1
print(*myarr)

for i in edges:
    if abs(cost[i[1]-1]-cost[i[0]-1])==i[2]:
        true_false.append('YES')
    else:
        true_false.append('NO')
print(true_false)