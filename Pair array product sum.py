for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    ones=0;twos=0
    for i in s:
        if i==1:
            ones+=1
        elif i==2:
            twos+=1
    n-=ones
    print(n*(n-1)//2-twos*(twos-1)//2)