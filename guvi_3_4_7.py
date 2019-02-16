s = list(input())
i = 0
j = len(s)-1
flag=True
while i<j:
    if s[i]!=s[j]:
        if flag==True:
            flag=False
            if s[i]==s[j-1]:
                j-=1
            else:
                i+=1
        else:
            break    
    else:
        i+=1;j-=1
print('YES') if flag else print('NO')