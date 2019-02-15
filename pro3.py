# LRU
n = int(input())
l = []
lsize = int(input())
s = list(map(int,input().splti()))
count=0
for i in s:
    if i in l:
        l.remove(i)
        l.append(i)
    else:
        l.append(i)
        if len(l)>lsize:
            l.pop(0)
        count+=1
print(count)