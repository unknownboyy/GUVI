t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    pwd=s[0];count=1
    flag=False
    indices = []
    prefix = s[:2]
    prefix_length = 2
    for i in range(n):
        if s[0]==s[i]:
            indices.append(i)
    while True:
        for i in indices:
            if (i+prefix_length)<=n and s[i:i+prefix_length]==prefix and prefix_length<=n//2:
                pass
            else:
                flag=True
                break
        if flag:
            break
        else:
            pwd=prefix
            prefix_length+=1
            prefix=s[:prefix_length]
    print(pwd) if len(indices)>1 else print(s)