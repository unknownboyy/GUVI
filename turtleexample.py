for _ in range(int(input())):
    k=int(input())
    n=int(input())
    s=list(map(int,input().split()))
    w=max(s)-min(s)-2*k
    if w<0:
        w+=k
    print(w)