for target_list in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    count=1;add=s[0]
    i=1
    while add<n-i:
        mysum=sum(s[i:min(i+add,n)])
        if mysum==0:
            mysum=add
        add+=mysum
        i=i+add-1
        count+=1
    print(count)

    