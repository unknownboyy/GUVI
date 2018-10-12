for target_list in range(int(input())) :
    n=int(input())
    seq=list(map(int,input().split()))
    myseq=list(map(int,input().split()))
    for i in range(n):
        myseq[i]-=seq[i]
    flag=True
    i=0
    while i<n and myseq[i]==0:
        i+=1
    while i<n-2:
        if myseq[i]>0:
            myseq[i]-=1
            myseq[i+1]-=2
            myseq[i+2]-=3
        i+=1
    for i in range(n):
        if myseq[i]!=0:
            flag=False;break
    print('TAK') if flag else print('NIE')