n = int(input())
s = list(map(int,input().split()))
s.sort()
w = []
while len(s)>0:
    w.append(s.pop())
    if len(s)>0:
        w.append(s.pop(0))
print(*w)