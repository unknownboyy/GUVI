for _ in range(int(input())) :
    s=input()
    l=len(s)//2
    d=dict()
    for i in s:
        if i in d:  d[i]+=1
        else:
            d[i]=1
    flag=True
    for i in d:
        if d[i]>l:
            flag=False;break
    print(1) if flag else print(0)