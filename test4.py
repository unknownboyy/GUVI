for _ in range(int(input())) :
    s=input()
    s=list(s.lower())
    while len(s)>0:
        ele=s[0]
        i=0;count=0
        while len(s)>0 and s[0]==ele:
            s.pop(0)
            count+=1
        print(str(count)+ele,end='')
    print('')