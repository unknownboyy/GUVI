# HackerEarth Aerobus
n = int(input())
s = list(map(int,input().split()))
a=0;b=0;c=0;d=0
for i in s:
    if a^i>a:
        a^=i
    elif b^i>b:
        b^=i
    elif c^i>c:
        c^=i
    elif d^i>d:
        d^=i
    else:
        diff1 = abs(a-a^i)
        diff2 = abs(b-b^i)
        diff3 = abs(c-c^i)
        diff4 = abs(d-d^i)
        diff = min(diff1,diff2,diff3,diff4)
        if diff == diff1:
            a^=i
        elif diff==diff2:
            b^=i
        elif diff==diff3:
            c^=i
        else:
            d^=i
print(a+b+c+d)


for _ in range(int(input())):
    n = int(input())
    days = 0
    while n!=1:
        if n%2==0:
            n//=2
            days+=1
        else:
            n-=1
            days+=1
    print(days)
