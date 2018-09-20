n,m,k=map(int,input().split())
s=[]
su=0
for _ in range(n) :
    s.append(list(map(int,input().split())))
    su+=sum(s[-1])
print()