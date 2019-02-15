f=1
n=int(input())
if n==0 or n==1:
    print(1)
else:
    for i in  range(2,n+1):
        f=f*i
    print(f)