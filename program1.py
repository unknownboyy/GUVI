def columnsearch(s,col,m,k):
    i=0;j=m-1
    if s[i][col]==k or s[j][col]==k:    return True
    mid=(i+j)//2
    while i<j:
        mid=(i+j)//2
        if s[mid][col]>k:
            j=mid-1
        elif s[mid][col]<k:
            i=mid+1
        else:
            return True
    if s[mid][col]==k:
        return True
    else:
        return False
def findk(s,m,n,k):
    i=0
    while i<n and s[0][i]<=k:
        if columnsearch(s,i,m,k):   return True
        i+=1
    return False
m,n=map(int,input().split())
s=[]
for i in range(m) :
    s.append(list(map(int,input().split())))
k=int(input())
if findk(s,m,n,k):
    print('Found')
else:
    print('Not Found')