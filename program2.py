# Chef and a Beautiful Digit
def func(s,element,send_index):
    localcount = 0
    new_index = send_index
    for i in range(send_index,len(s)):
        if s[i]==element:
            localcount+=1
            new_index = i
    return (localcount,new_index)
for _ in range(int(input())):
    s,d =  input().split()
    s = list(s)
    minset = set()
    min_list = []
    for i in s:
        if i<d:
            min_list.append(i)
            minset.add(i)
    if len(minset)==0:
        print(min("".join(s),d*len(s)))
    else:
        l = sorted(list(minset))
        send_index = 0
        new_string = ''
        for i in l:
            count,send_index = func(s,i,send_index)
            new_string+=count*i
        print(new_string+d*(len(s)-len(new_string)))