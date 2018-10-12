for target_list in range(int(input())) :
    s=input()
    s=s.lower()
    p=list(filter(lambda x: (ord(x)>=48 and ord(x)<=57) or (ord(x)>=97 and ord(x)<=122) ))
    if p==p[::-1]:
        print('YES')
    else:
        print('NO')