for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    s1=list(filter(lambda x:x%2==0,s));s1.sort()
    s2=list(filter(lambda x:x%2==1,s));s2.sort(reverse=True)
    print(*s2,*s1)