for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    f = 1
    if n<3:
        print(n)
    elif sum(s)==n:
        print(n)
    else:
        for i in range(n-2):
            f*=s[i]
        print((f+n)%(10**9+7))