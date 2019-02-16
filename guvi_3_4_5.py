s = list(input())
flag=True
if len(s)%2==0:
    print('NO')
else:
    i=0;j=len(s)//2
    while i<len(s)//2 and j<len(s):
        if s[i]!=s[j]:
            if flag:
                flag=False
                if s[i]==s[j+1]:
                    j+=1
                else:
                    i+=1
            else:
                break
        else:
            i+=1;j+=1
    print('YES') if flag else print('NO')