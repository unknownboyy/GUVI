n=int(input())
s=list(map(int,input().split()))
for i in range(n):
    if i+1!=s[i]:
        print(s[i]);break