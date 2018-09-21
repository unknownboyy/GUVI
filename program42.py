a,b=map(int,input().split())
c,d=map(int,input().split())
if a==c:
    print(a)
elif a>c and b>=d:
    print(-1)
elif a<c and b<=d:
    print(-1)
else:
    x1=a;x2=b
    