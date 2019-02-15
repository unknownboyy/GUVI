t = int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s = list(map(int,input().split()))
    x = 0
    for i in s:
        x^=i
    if x==0:
        print('Second')
    else:
        print('First')