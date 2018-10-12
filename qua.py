for target_list in range(int(input())) :
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    s.sort(reverse=True)
    l=s[k-1]
    count=0
    for i in s:
        if i>=l:
            count+=1
    print(count)