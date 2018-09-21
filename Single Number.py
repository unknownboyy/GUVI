for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    c=[0]*51
    for i in s:
        c[i]+=1
    for i in range(51):
        if c[i]%2==1:
            print(i)