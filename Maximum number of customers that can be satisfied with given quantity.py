for _ in range(int(input())):
    n,k=map(int,input().split())
    a,b=map(int,input().split())
    s=[]
    for i in range(n):
        x,y=map(int,input().split())
        s.append([x,y,x*a+y*b,i+1])
    s=sorted(s,key=lambda x:(x[2],x[3]))
    i=0
    while i<n and k>=s[i][2]:
        k-=s[i][2]
        i+=1
    print(i)
    for j in range(i):
        print(s[j][3],end=' ')
    if i>0:
        print('')