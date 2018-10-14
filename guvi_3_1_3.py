n=int(input())
s=list(map(int,input().split()))
dd=[]
for i in range(n):
    if i==s[i]: dd.append(i)
print(*sorted(dd)) if len(dd)>0 else print(-1)