f=[7]
for i in range(1,120):
    f.append(f[-1]*2+i)
for _ in range(int(input())) :
    n=int(input())
    print(f[n-1]%(10**9+7))