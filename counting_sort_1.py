n=int(input())
c=[0]*100
s=list(map(int,input().split()))
for i in s:
    c[i]+=1
print(*c)