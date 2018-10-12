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

# for _ in range(int(input())) :
#     pass 
#     n,m=map(int,input().split())
#     s=[[] for i in range(n)]
#     for _ in range(m) :
#         x,y,w=map(int,input().split())
#         s[x-1].append([y-1,w])
#         s[y-1].append([x-1,w])
#     for i in range(n) :
#         li=s[i]
#         if len(li)>0:
#             li=sorted(li,key=lambda x:(x[0],x[1]))
#             new_li=[]
#             new_li.append(li[0])
#             for j in range(1,len(li)):
#                 if li[j][0]==li[j-1][0]:
#                     pass
#                 else:
#                     new_li.append(li[j])
#             s[i]=new_li



t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    c=[[1000000 for x in range(n)] for x in range(n)]
    for i in range(m):
        a,b,s=map(int,input().split())
        c[a-1][b-1]=min(c[a-1][b-1],s)
        c[b-1][a-1]=min(c[a-1][b-1],s)
    s=[[] for j in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if c[i][j]!=1000000:
                s[i].append([j,c[i][j]])
                s[j].append([i,c[i][j]])
    k=int(input())
    myarr=doDijksatra(s,k-1,n)
    for i in range(n):
        if myarr[i]==10**6+1:
            myarr[i]=-1
    myarr.pop(k-1)
    print(*myarr)