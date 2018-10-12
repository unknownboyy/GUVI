for target_list in range(int(input())) :
    string=input()
    ch=input()
    c=int(input())
    if c==0:
        print(string)
    else:
        i=0
        while i<len(string):
            if string[i]==ch:
                c-=1
            i+=1
            if c==0:
                break
        if i==len(string):
            print('Empty string')
        else:
            print(string[i:])