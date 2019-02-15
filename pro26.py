for _ in range(int(input())):
    s1=[]
    for h in range(int(input())):
        s=[]
        n=input()
        for i in range(len(n)):
            if n[i] not in s:
                s.append(n[i])
        w=s
        if s1!=[]:
            k=s1
            w=[]
            for i in s:
                if i in k:
                    w.append(i)
                    s1=w
        else:
            s1=s 
    print(len(w))