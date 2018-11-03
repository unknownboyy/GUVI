for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if len(a)!=len(b):
        print('Alice')
    else:
        print('Bob')