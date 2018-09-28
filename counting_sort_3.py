n=int(input())
c=[0]*100
for _ in range(n):
    a,b=input().split()
    c[int(a)]+=1
for i in range(1,100) :
    c[i]+=c[i-1]
print(*c)