visited_shop=0

def get_min_cost_shop(cost,visited):
    cc=10**6+1;cind=0
    for i in range(len(cost)):
        if cost[i]<cc and visited[i]==False:
            cc=cost[i];cind=i
    return cind+1

def move_little_cat(cc,s,pos_of_little,little_cat_time,k,visited_little):
    global visited_shop
    little_cur_cost=10**6+1;target_ind=0;costst=10**6+1
    for i in s[pos_of_little]:
        if visited_little[i[0]-1]==False and i[1]<little_cur_cost:
            little_cur_cost=i[1];target_ind=i[0]
    visited_shop=visited_shop|k[target_ind]
    little_cat_time+=little_cur_cost
    visited_little[target_ind]=True
    print('little_cat_move',k[target_ind],little_cat_time,visited_little[target_ind])
    return visited_little,little_cat_time

def move_big_cat(cc,s,pos_of_big,big_cat_time,k,visited_big):
    global visited_shop
    big_cur_cost=10**6+1;target_ind=0;costst=10**6+1
    for i in s[pos_of_big]:
        if visited_big[i[0]-1]==False and i[1]<big_cur_cost:
            big_cur_cost=i[1];target_ind=i[0]
    visited_shop=visited_shop|k[target_ind]
    big_cat_time+=big_cur_cost
    visited_big[target_ind]=True
    print('big_cat_move',k[target_ind],big_cat_time,visited_big[target_ind])
    return visited_big,big_cat_time

n,m,kk=map(int,input().split())
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
visited_little=[False]*n
visited_big=[False]*n
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
little_cat=1
big_cat=1
little_cat_time=0
big_cat_time=0
tt=0
while visited_shop<2**kk-1:
    if little_cat_time<=big_cat_time:
        visited_little,little_cat_time=move_little_cat(cc,s,little_cat,little_cat_time,k,visited_little)
    else:
        visited_big,big_cat_time=move_big_cat(cc,s,big_cat,big_cat_time,k,visited_big)
    tt+=1
    if tt==5:
        break
print(max(little_cat_time,big_cat_time))
print(visited_shop)
print(little_cat_time,big_cat_time)