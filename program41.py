def solution (a, b, n):
    i = 0
    while i * a <= n: 

        if (n - (i * a)) % b == 0: 
            return [i,int((n - (i * a)) / b)]
        i = i + 1
    return None 
d1,a1=map(int,input().split())
d2,a2=map(int,input().split())
a=-d1;b=d2;c=a1-a2+d2-d1
if a1==a2:
    print(a1)
elif a1>a2 and d1>=d2:
    print(-1)
elif a1<a2 and d1<=d2:
    print(-1)
else:
    g=solution(a,b,c)
    if g!=None:
        print(a1+(g[0]-1)*d1)