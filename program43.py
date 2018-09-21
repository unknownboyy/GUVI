n=int(input())
s=list(input())
count=0
i=0
while i<n-1:
    if s[i]=='V' and s[i+1]=='K':
        if s[0]!='V':
            s[i],s[i+1]=s[i+1],s[i]
            i-=1
            count+=1
        else:
            s[i+1],s[i+2]=s[i+2],s[i+1]
            i+=1
            count+=1
    else:
        i+=1
print(count)