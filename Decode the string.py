def getSol(s):
    if len(s)<3:
        return ""
    else:
        ss=""
        s=s[1:-1]
        while len(s)>0 and  ord(s[0])>=97 and ord(s[0])<=122:
            ss=ss+s[0]
            s=s[1:]
        cc=0
        while  len(s)>0 and s[0]!='[':
            cc=cc*10+int(s[0])
            s=s[1:]
        if cc==0:   cc=1
        return ss+cc*getSol(s)
for target_list in range(int(input())) :
    s=input()
    cc=0
    while s[0]!='[':
        cc=cc*10+int(s[0])
        s=s[1:]
    if cc==0:
        cc=1
    print(cc*getSol(s))
    