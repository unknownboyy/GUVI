myprimes=[1]*201
for i in range(2,200+1):
    if myprimes[i]==1:
        for j in range(i+i,200+1,i):
            myprimes[j]=0
semiprimes=[0]*250
for i in range(2,201):
    for j in range(2,201):
        if myprimes[i] and myprimes[j] and i*j<250 and i!=j:
            semiprimes[i*j]=1
t=int(input())
for _ in range(t) :
    n=int(input());x=0
    for i in range(2,n-2):
        if semiprimes[i] and semiprimes[n-i]:
            x=1;break
    if x==1:
        print('YES')
    else:
        print('NO')
