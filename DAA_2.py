n=int(input())
s=list(map(int,input().split()))
c=[0]*(max(s)+1)
for i in s:
    c[i]+=1
a=[0]*n
for i in range(1,max(s)+1) :
    c[i]+=c[i-1]
for i in range(n-1,-1,-1):
    a[c[s[i]]-1]=s[i]
    c[s[i]]-=1
print(*a)