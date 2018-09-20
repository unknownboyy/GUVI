for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    low1=0;low2=0
    s.sort()
    for i in range(n):
        if i%2==0:
            low1=low1*10+s[i]
        else:
            low2=low2*10+s[i]
    print(low1+low2)