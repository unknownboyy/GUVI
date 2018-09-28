f=[0]*(160001)
d=[i**2 for i in range(400)]
for i in range(399):
    for j in range(i+1,400):
        f[d[j]-d[i]]=1
t=int(input())
for _ in range(t) :
    n=int(input())
    s=list(map(int,input().split()))
    z=0
    loser=True
    while len(s)>0:
        for i in s:
            if f[z+i]:
                s.remove(i);loser=not(loser)
                break
        else:
            break
    print('Ghayeeth') if not(loser) else print('Siroj')

