shortest_path=[[10**8 for i in range(1050)] for i in range(1050)]
shops=[0]*1050
graph=[[] for i in range(1050)]
queue=[]
def topop(ll):
    first=10**8+1;indexx=0
    for i in range(len(ll)):
        if first>ll[i][0]:
            first=ll[i][0]
            indexx=i
    return indexx
def InQueue(node,mask,cost):
    if shortest_path[node][mask]<=cost:
        return
    current=[shortest_path[node][mask],[node,mask]]
    if current in queue:
        queue.remove(current)
    shortest_path[node][mask]=cost
    current[0]=cost
    queue.append(current)

def Dijkstra(src):
    InQueue(src,shops[src],0)
    while len(queue)>0:
        x=topop(queue)
        app=queue.pop(x)
        cost=app[0]
        current_shops=app[1][1]
        src=app[1][0]
        for neighbour in graph[src]:
            InQueue(neighbour[0],current_shops|shops[neighbour[0]],cost+neighbour[0])

n_cities,n_roads,fishes_types_no=map(int,input().split())
for i in range(1,n_cities+1):
    t_list=list(map(int,input().split()))
    t=t_list.pop(0)
    for j in t_list:
        shops[i]|=(1<<(j-1))
for _ in range(n_roads):
    fromm,to,cost=map(int,input().split())
    graph[fromm].append([to,cost])
    graph[to].append([fromm,cost])
    
Dijkstra(1)

best_time=10**8+1
for i in range(1<<fishes_types_no) :
    for j in range(i,1<<fishes_types_no):
        if (i|j) == ((1<<fishes_types_no)-1):
            best_time=min(best_time,max(shortest_path[n_cities][i],shortest_path[n_cities][j]))
print(best_time)
for i in range(6):
    print(shortest_path[n_cities][i])
