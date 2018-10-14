s1,s2=input().split()
column=len(s1)+1
row=len(s2)+1
c=[[0 for i in range(column)] for i in range(row)]
for i in range(1,row):
    c[i][0]=i
for i in range(1,column):
    c[0][i]=i
for i in range(1,row):
    for j in range(1,column):
        if s2[i-1]==s1[j-1]:
            c[i][j]=min(c[i-1][j-1],c[i-1][j],c[i][j-1])
        else:
            c[i][j]=min(c[i-1][j-1],c[i-1][j],c[i][j-1])+1
print(c[row-1][column-1])