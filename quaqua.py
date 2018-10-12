f=[True]*101
for i in range(2,100+1):
    if f[i]:
        for j in range(i+i,100+1,i):
            f[j]=False
pp=[False]*201
for i in range(2,101):
    for j in range(2,101):
        if f[i] and f[j] and i*j<201 and i!=j:
            pp[i*j]=True
for target_list in range(int(input())) :
    n=int(input())
    flag=False
    for i in range(2,n-2):
        if pp[i] and pp[n-i]:
            flag=True;break
    print('YES') if flag else print('NO')
