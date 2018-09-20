for _ in range(int(input())):
    n=int(input())
    arrival_time=list(map(int,input().split()))
    depart_time=list(map(int,input().split()))
    train_order=[]
    for i in range(n):
        train_order.append(['a',arrival_time[i]])
        train_order.append(['d',depart_time[i]])
    train_order=sorted(train_order,key=lambda x:x[1])
    max_plaform_needed=0
    temp_result=0
    for i in range(2*n):
        if train_order[i][0]=='a':
            temp_result+=1
        else:
            temp_result-=1
        max_plaform_needed=max(max_plaform_needed,temp_result)
    print(max_plaform_needed)