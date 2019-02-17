try:
    n = int(input())
    s = list(map(int,input().split()))
    curr = 1
    c = [1]*n
    for i in range(n-2,-1,-1):
        if s[i]*s[i+1]<0:
            curr+=1
            c[i]=max(curr,c[i+1])
        else:
            c[i]=max(curr,c[i+1])
            curr=0
    print(*c)
except:
    print('Invalid Input')