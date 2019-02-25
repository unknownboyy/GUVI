t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    s.sort()
    count = 0
    for i in range(n):
        if s[i]<=count:
            count+=1
    print(count)