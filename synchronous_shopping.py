def get_min_cost_shop(cost,visited):
    cc=10**6+1;cind=0
    for i in range(len(cost)):
        if cost[i]<cc and visited[i]==False:
            cc=cost[i];cind=i
    return cind+1
n,m,k=map(int,input().split())
shops=[]
for i in range(n):
    shops.append(list(map(int,input().split())))
k=[0]*n
for i in range(n):
    for j in shops[i][1:]:
        k[i]=k[i]|1<<(j-1)
print(*k)
s=[[] for i in range(n+1)]
cc=[[10**6 for i in range(n+1)] for i in range(n+1)]
for i in range(m):
    x,y,w=map(int,input().split())
    s[x].append([y,w])
    s[y].append([x,w])
    cc[x][y]=w
    cc[y][x]=w
    
visited=[False]*n
source=1
cost=[10**6]*n
cost[0]=0
q=n
while q>0:
    app=get_min_cost_shop(cost,visited)
    visited[app-1]=True
    for i in s[app]:
        target,tcost=i
        cost[target-1]=min(cost[app-1]+tcost,cost[target-1])
    q-=1
print(cost)