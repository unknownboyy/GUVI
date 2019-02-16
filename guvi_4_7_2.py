def lcs(s1,s2):
    l1 = len(s1) +1
    l2 = len(s2) +1
    c = [[0 for i in range(l1)] for i in range(l2)]
    for i in range(l1):
        c[0][i]=0
    for i in range(l2):
        c[i][0]=0
    for i in range(1,l2):
        for j in range(1,l1):
            if s1[i-1]==s2[j-1]:
                c[i][j]=c[i-1][j-1]+1
            else:
                c[i][j]=max(c[i-1][j],c[i][j-1])
    return c[l2-1][l1-1]
a = input().strip()
if len(a)==0:
    print('Invalid Input')
else:
    print(len(a)-lcs(a,a[::-1]))