"""
file= open("file.txt")
d=dict()
for i in file:
    for j in i.split():
        if j in d:
            d[j]+=1
        else:
            d[j]=1
ll=list(d.keys())
lll=[]
for i in ll:
    lll.append([i,i.lower()])
lll = sorted(lll,key=lambda x:x[1])
print(lll)
for i in lll:
    if i[0] in d:
        print(i[0],d[i[0]])
        del d[i[0]]
"""
"""
ll = list(map(int,list(filter(lambda x:x%1==0,list(map(float,input().split()))))))
print(ll)
"""