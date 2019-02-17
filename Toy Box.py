n,m=map(int,input().split())
s = set()
total_sum = 0
w = []
for i in range(n):
    x = list(map(int,input().split()))
    w.append(x)
w.sort(key=lambda x:x[0],reverse=True)
for i in range(n):
    if w[i][1] not in s:
        s.add(w[i][1])
        total_sum+=w[i][0]
print(total_sum)