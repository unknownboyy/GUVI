for _ in range(int(input())) :
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    d=dict()
    jaroori=0
    faaltu=0
    for i in s:
        if i in d:
            faaltu+=1
            d[i]+=1
        else:
            d[i]=1
            jaroori+=1
    if k<=faaltu:
        print(jaroori)
    else:
        print(jaroori-(k-faaltu))
