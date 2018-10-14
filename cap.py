cost=0
def go_for_dfs(s,row_size,col_size,i,j,color):
    pass
string=input()
rows=list(string.split("#"))
s=[]
for i in rows:
    s.append(list(map(int,i.split("@"))))
col_size=len(s[0])
row_size=len(s)
color=[[False for i in range(col_size)] for i in range(row_size)]
for i in range(row_size):
    for j in range(col_size):
        if s[i][j]==-1:
            color[i][j]=True
for i in range(row_size):
    for j in range(col_size):
        if s[i][j]==-1:
            s,color=go_for_dfs(s,row_size,col_size,i,j,color)