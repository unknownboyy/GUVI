n,k=map(int,input().split())
s=list(map(int,input().split()))
ss=[]
s.sort()
ss.append(s.pop(0))

for j in s:
    upto=len(s)
    count=0
    ele=s[j]
    for i in ss:
        if ele%i==0:
            count=0
            break
    if count==upto:
        ss.append(ele)
print(len(ss))