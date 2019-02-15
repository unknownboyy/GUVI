def now_sort(s):
    s.sort()
    print("?",*s[:5])
    third,fourth = map(int,input().split())
    s[2],s[s.index(third)] = third,s[2]
    s[3],s[s.index(fourth)] = fourth,s[3]

    a,b=map(int,input().split())
    if a!=s[2] or b!=s[3]:
        pass


for _ in range(int(input())):
    n=int(input())
    s=[i+1 for i in range(n)]
    while n>6:
        print("?",*s[:5],flush=True)
        x,y = map(int,input().split())
        s.remove(x)
        n-=1
    now_sort(s)
    """
    print("?",*s)
    third,fourth = map(int,input().split())
    s[2],s[s.index(third)] = third,s[2]
    s[3],s[s.index(fourth)] = fourth,s[3]

    a,b=map(int,input().split())
    if not (third==a and fourth==b):
        print('?',*s)
        a,b=map(int,input().split())
    """