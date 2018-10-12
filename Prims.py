def getMinCostNode(cost,visited):
    myCost=10**6+2;node=-1
    for i in range(len(visited)):
        if visited[i]==False and cost[i]<myCost:
            myCost=cost[i]
            node=i
    return node
def findPrims(s,k,n):
    visited=[False]*n
    cost=[10**6+1]*n
    cost[k]=0
    q=n
    totalcost=0
    while q>0:
        app=getMinCostNode(cost,visited)
        totalcost+=cost[app]
        visited[app]=True
        for i in s[app]:
            cost[i[0]]=min(cost[i[0]],i[1])
        q-=1
    #print(cost)
    return totalcost
    
n,m=map(int,input().split())
s=[[] for i in range(n)]
for _ in range(m) :
    x,y,w=map(int,input().split())
    s[x-1].append([y-1,w])
    s[y-1].append([x-1,w])
k=int(input())
print(findPrims(s,k-1,n))