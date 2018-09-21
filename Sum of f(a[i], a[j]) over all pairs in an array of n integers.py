for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    count=0
    for i in range(n-1):
        for j in range(i+1,n) :
            if s[j]-s[i]>1:
                count+=(s[j]-s[i])
    print(count)