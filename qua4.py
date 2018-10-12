fact=[1,1]
for i in range(2,10**6):
    fact.append((i*fact[-1])%(10**9+7))
for target_list in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    c=[0]*(10**6+1)
    for i in s:
        c[i]+=1
    cc=c.copy()
    for i in range(1,10**6+1):
        cc[i]+=cc[i-1]
    for i in range(10**6,-1-1):
        if c[i]>0:
            pass
    i=10**6
    count=1
    while i>=0 and c[i]==0:
        i-=1
    team_can_form=c[i]
    i-=1
    while i>=0:
        while c[i]==0:
            i-=1
        mymin=min(c[i],team_can_form)
        mymax=max(c[i],team_can_form)
        # count=(count*fact[mymin])%(10**9+7)
        # print(fact[mymin])
        print(count,mymax)
        count=count*mymax
        team_can_form-=0
        c[i]-=mymin
        team_can_form=team_can_form+c[i]
        i-=1
    print(count%(10**9+7))