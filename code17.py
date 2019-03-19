def coin(n,arr):
    c = [0]*(n+1)
    c[0]=1
    for i in arr:
        for j in range(1,n+1):
            if j>=i:
                c[j]+=c[j-i]
    return c[n]
n = int(input())
s = list(map(int,input().split()))
summ = int(input())
print('Total number of solutions are',coin(summ,s))