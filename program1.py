s = [[0,0,0,0],[0,1,1,0],[0,0,1,0],[0,1,0,1]]
w = []
for i in range(4):
    w.append(s[i].copy())
n=4
onemin,onemax,zeromin,zeromax = [int(i) for i in input().strip().split()]
k = int(input())
for _ in range(k):
    for i in range(4):
        for j in range(4):
            one = 0
            if i>0 and j>0:
                one+=s[i-1][j-1]
                #print(one,i-1,j-1,'add',s[i-1][j-1])
            if i>0:
                one+=s[i-1][j]
                #print(one,i-1,j,'add',s[i-1][j])
            if i>0 and j<n-1:
                one+=s[i-1][j+1]
                #print(one,i-1,j+1,'add',s[i-1][j+1])
            if j>0:
                one+=s[i][j-1]
                #print(one,i,j-1,'add',s[i][j-1])
            if j<n-1:
                one+=s[i][j+1]
                #print(one,i,j+1,'add',s[i][j+1])
                #print(s)
            if i<n-1 and j>0:
                one+=s[i+1][j-1]
                #print(one,i+1,j-1,'add',s[i+1][j-1])
            if i<n-1:
                one+=s[i+1][j]
                #print(one,i+1,j,'add',s[i+1][j])
            if i<n-1 and j<n-1:
                one+=s[i+1][j+1]
                #print(one,i+1,j+1,'add',s[i+1][j+1])
            if s[i][j]==1:
                if one>=onemin and one<=onemax:
                    w[i][j]=1
                else:
                    w[i][j]=0
            else:
                if zeromin<=one and one<=zeromax:
                    w[i][j]=1
                else:
                    w[i][j]=0
            #print('i=',i,'j=',j,one)
    s = []
    for i in range(4):
        s.append(w[i].copy())
for i in s:
    print(*i)