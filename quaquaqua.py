for target_list in range(int(input())) :
    n=int(input())
    seq=list(map(int,input().split()))
    myseq=list(map(int,input().split()))
    flag=True
    i=n-1;decby=myseq[i]
    while i>=0:
        if myseq[i]>decby or myseq[i]-decby>0:
            decby=myseq[i]-decby-1
            myseq[i]=0
        else:
            myseq[i]-=decby
            decby-=1
        if myseq[i]<seq[i]:
            flag=False;break
        i-=1
    print('TAK') if flag else print('NIE')