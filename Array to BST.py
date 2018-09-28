c=[]

def myprint(l,r,s):
    if l<=r:
        y=(l+r)//2
        if c[y]:
            print(s[y],end=' ');c[y]=False
            myprint(l,y-1,s)
            myprint(y+1,r,s)

for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    c=[True]*n
    print(s[(n-1)//2],end=' ');c[(n-1)//2]=False
    myprint(0,(n-1)//2-1,s)
    myprint((n-1)//2+1,n-1,s)
    print('')