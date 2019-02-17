try:
    n,t=map(int,input().split())
    s = [int(i) for i in input().strip().split()]
    i=0
    while i<n and t>0:
        t-=(86400-s[i]);i+=1
    print(i)
except:
    print('Invalid Input')