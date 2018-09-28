n=int(input())
s=list(map(int,input().split()))
c=[0]*(max(s)+1)
for i in s:
    c[i]+=1
for i in range(max(s)+1):
    for j in range(c[i]):
        print(i,end=' ')