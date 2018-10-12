for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    if n%2==1:
        print('NO')
    else:
        d1=s[:n//2]
        d2=s[n//2:]
        flag=True
        ss=[]
        for i in range(n//2):
            if d1[i]==-1 or d2[i]==-1:
                if d1[i]==-1:
                    ss.append(d2[i])
                else:
                    ss.append(d1[i])
            else:
                if d1[i]!=d2[i]:
                    flag=False
                    break
                else:
                    ss.append(d1[i])
    if flag:
        print('YES')
        print(*ss,*ss)
    else:
        print('NO')