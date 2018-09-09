p=[True]*(10**6+1)
for i in range(2,int((10**6)**0.5)+1):
    if p[i]:
        for j in range(i+i,10**6+1,i):
            p[j]=False
p[0]=False;p[1]=False

parity=[0,1]
for i in range(2,10**6+1):
    rr=sum(list(map(int,list(bin(i)[2:]))))
    if rr%2==0:
        parity.append(0)
    else:
        parity.append(1)

print(*parity)
def isprimesum(n):
    for k in  range(2,n//2+1):
        if p[k] and p[n-k] and parity[k]==parity[n-k] : return True
        #if p[k] and p[n-k]: return True
    return False
t=int(input())
for _ in range(t) :
    n=int(input())
    count=0
    s=list(map(int,input().split()))
    for i in range(n-1):
        for j in range(i+1,n):
            xy=s[i]^s[j]
            if isprimesum(xy):  count+=1#;print(i+1,j+1)
            #if isprimesum(xy) and parity[s[i]]==parity[s[j]]:  count+=1;print(s[i],s[j])
    #print(count)
