for target_list in range(int(input())) :
    n=input()
    ss=[]
    s=list(input().split())
    for i in range(0,2*n,2):
        ss.append([s[i],int(s[i+1])])
    ss=sorted(ss,key=lambda x:(x[1],x[0]))
    s=[]
    for i in range(n):
        s.append(ss[i][0])
        s.append(ss[i][1])
    print(*s)