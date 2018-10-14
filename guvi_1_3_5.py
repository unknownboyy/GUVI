n=int(input())
s=list(map(int,input().split()))
if n%2==1:
    print(s[n//2])
else:
    print((s[n//2]+s[n//2+1])/2)