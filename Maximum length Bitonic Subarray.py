def leftbit(s):
    count=1;tempcount=1
    if len(s)==1:   return 1
    i=1;l=len(s)
    while i<l and s[i]<s[i-1]:
        i+=1
    if i==l:    return l
    count=i;tempcount=2;phase=True
    for j in range(i,l):
        if s[j]>s[j-1]:
            if phase==True:
                tempcount+=1
            else:
                count=max(count,tempcount)
                tempcount=2
                phase=True
        else:
            if phase==False:
                tempcount+=1
            else:
                tempcount+=1
                count=max(count,tempcount)
                tempcount=1
                phase=False
    return max(count,tempcount)
def rightbit(s):
    count=1;tempcount=1
    if len(s)==1:   return 1
    i=1;l=len(s)
    while i<l and s[i]>s[i-1]:
        i+=1
    if i==l:    return l
    count=i;tempcount=2;phase=True
    for j in range(i,l):
        if s[j]>s[j-1]:
            if phase==True:
                tempcount+=1
            else:
                count=max(count,tempcount)
                tempcount=2
                phase=True
        else:
            if phase==False:
                tempcount+=1
            else:
                tempcount+=1
                count=max(count,tempcount)
                tempcount=1
                phase=False
    
    return max(count,tempcount)

t=int(input())
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    print(max(leftbit(s),rightbit(s)))