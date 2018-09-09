from random import randint
n=int(input())
p=[i+1 for i in range(n)]
for i in range(n):
    j=randint(1,n)-1
    p[i],p[j]=p[j],p[i]
print(*p)