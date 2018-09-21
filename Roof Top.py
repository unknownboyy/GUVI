for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    previous_true=True
    max_count=0
    count=0
    for i in range(1,n):
        if s[i]>s[i-1]:
            count+=1
        else:
            max_count=max(count,max_count)
            count=0
    print(max(count,max_count))