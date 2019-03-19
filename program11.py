for _ in range(int(input())):
    n,k = map(int,input().split())
    s = list(map(int,input().split()))
    flag=False
    for i in range(n-1,-1,-1):
        penalty = 0
        for j in range(i,n):
            penalty+=int(s[j]/(j+1))
        print('Penalty',penalty,'For',i+1)
        if penalty>k:
            flag=True
            break
    if flag:
        print(n-i-1)
    else:
        print(n+1)