count = 0
def dfs(s,ss,visited):
    global count
    count+=1
    for i in s[ss]:
        if visited[i]==False:
            visited[i]=True
            dfs(s,i,visited)
n,m,k=map(int,input().split())
s=[[] for i in range(n)]
for i in range(m):
    x,y=map(int,input().split())
    s[x-1].append(y-1)
    s[y-1].append(x-1)
segment = 0
visited=[False]*n
w = 0
flag = False
for i in range(n):
    if visited[i]==False:
        dfs(s,i,visited)
        segment+=1
        if count>1:
            if count>=k:
                w+=(count-k-1)
                flag=True
            else:
                w+=(count-1)
        count=0
print(w) if flag else print(-1)