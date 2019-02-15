# Program for Operator Arrangement
answer = []
def count(current_index,mylist,cur_val,value,operator_list):
    if current_index<len(mylist):
        count(current_index+1,mylist,cur_val+mylist[current_index],value,operator_list+['+'])
        count(current_index+1,mylist,cur_val-mylist[current_index],value,operator_list+['-'])
    else:
        if cur_val==value:
            answer.append(operator_list)

n = int(input())
s = list(map(int,input().split()))
value = s.pop()
count(0,s,0,value,[])
print(len(answer))
for i in answer:
    for j in range(n-1):
        print(i[j],s[j],sep='',end='')
    print('=',value,sep='')