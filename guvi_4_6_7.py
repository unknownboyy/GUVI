try:
    a = input()
    b = input()
    l1 = len(a);l2=len(b)
    flag=False
    for i in range(l1-1):
        for j in range(l2-1):
            if a[i]==b[j] and a[i+1]==b[j+1]:   flag=True;break
        if flag:
            break
    print('yes') if flag else print('no')
except:
    print('Invalid Input')