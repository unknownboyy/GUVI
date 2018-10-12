for target_list in range(int(input())) :
    s=input()
    a1=[]
    su=0
    for i in s:
        if ord(i)>=48 and ord(i)<=57:
            su+=int(i)
        else:
            a1.append(i)
    print("".join(a1)+str(su))