from math import ceil
for _ in range(int(input())):
    n,k = map(int,input().split())
    s = list(map(int,input().split()))
    count = 0
    for i in range(n):
        for j in range(i,n):
            multiplier = ceil(k/(j-i+1))
            if s[i:j+1].count(sorted(s[i:j+1]*multiplier)[k-1]) in s[i:j+1]:
                count+=1
    print(count)