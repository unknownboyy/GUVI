q=[]
def bfs(s,k):
    global q
    q.append(k)
    visited=[False]*(len(s)+1)
    visited[k]=True
    while len(q)>0:
        ss=q.pop(0)
        print(ss,end=' ')
        for i in s[ss]:
            if visited[i]==False:
                visited[i]=True
                q.append(i)
n,m=map(int,input().split())
s=[[] for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    s[x].append(y)
    s[y].append(x)
k=int(input())
bfs(s,k)
