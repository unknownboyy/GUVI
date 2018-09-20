def func(s,i,j):
    while i<j:
        if s[i]>s[j]:
            i+=1
        elif s[i]<s[j]:
            j-=1
        else:
            return min(func(s,i,j-1),func(s,i+1,j))
    return s[j]
for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    print(func(s,0,n-1))