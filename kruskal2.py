def kruskal(s):
    pass
    
       


n,m=map(int,input().split())
s1=[]
for i in range(m):
    k=list(map(int,input().split()))
    s1.append(k)
s=sorted(s1,key=lambda x:x[2])
kruskal(s)