t=int(input())
for _ in range(t) :
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    f=[]
    for i in s:
        if i<=k:
            k-=i
            f.append("1")
        else:
            f.append("0")
    print("".join(f))