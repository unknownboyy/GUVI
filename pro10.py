for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    su = 0
    for i in range(n):
        if s[i]==-1:
            s[i] = su//(i)
        su+=s[i]
    print(*s)