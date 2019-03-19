f = [0,1]
for i in range(2,10**5+1):
    f.append((f[i-1]+f[i-2])%(10**9+7))
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans = (ans+f[a[i]+a[j]-a[k]])%(10**9+7)
    print(ans%(10**9+7))