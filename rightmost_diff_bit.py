for _ in range(int(input())) :
    a,b=map(int,input().split())
    m=1
    x=a^b
    pos=-1
    for i in range(32):
        if x&(m<<i):
            pos=i+1;break
    print(pos)