for target_list in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    s.sort()
    k=int(input())
    su=0
    for i in s:
        if i<=s[k-1]:
            su+=i
    print(su)
    print(*s)