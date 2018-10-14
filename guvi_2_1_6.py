d=dict()
x,y=input().split()
if len(x)!=len(y):
    print('no')
else:
    flag=True
    for i in range(len(x)):
        if x[i] in d and d[x[i]]!=y[i]: flag=False;break
        else:
            d[x[i]]=y[i]
    if flag:    print('yes')
    else:
        print('no')