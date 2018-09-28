f=[1]*(10**6+1)
for i in range(2,10**6+1):
    for j in range(i,10**6+1,i):
        f[j]+=i
for i in range(1,10**6+1) :
    f[i]+=f[i-1]
for _ in range(int(input())) :
    n=int(input())
    print(f[n]-1)