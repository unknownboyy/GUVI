my_list = []
def func(i,s,max_day,till_sum,mm):
    if i==7:
        if mm==till_sum:    my_list.append(s)
    else:
        while i<7 and s[i]!='?':
            i+=1
        for j in range(1,max_day+1):
            func(i+1,s[:i]+str(j)+s[i+1:],max_day,till_sum+j,mm)
n = int(input())
max_day = int(input())
s = input()
till_sum = 0
for i in s:
    if i!='?':
        till_sum+=int(i)
i = 0
while i<7 and s[i]!='?':
    i+=1
func(i,s,max_day,till_sum,n)
print(*my_list,sep='\n')