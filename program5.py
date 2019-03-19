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
    elif len(minset)==1:
        print(min(minset)*s.count(min(minset))+d*(len(s)-s.count(min(minset))))
    else:
        m = min(minset)
        minset.remove(m)
        m2 = min(minset)
        i = len(s)-1
        count = 0
        while i>=0 and s[i]!=m:
            if s[i]==m2:
                count+=1
            i-=1
        print(m*s.count(m)+count*m2+d*(len(s)-s.count(m)-count))