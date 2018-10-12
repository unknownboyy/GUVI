li=[]
def getAllCombs(s,n):
    while len(li)>0:
        temp=li.pop()
        for i in range(n):
            if temp[i]=='?':
                temp[i]='1'
                li.append(temp)
                temp[i]='0'
                li.append(temp)
for _ in range(int(input())) :
    s=list(input())
    li=[]
    li.append(s)
    getAllCombs(s,len(s))
    print(*li)