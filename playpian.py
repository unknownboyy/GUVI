for _ in range(int(input())):
    s=input()
    a=0;b=0
    flag=True
    for i in range(len(s)):
        if s[i]=='A':
            a+=1
        else:
            b+=1
        if i%2==1 and a!=b:
            flag=False
            break
    print('yes') if flag else print('no')