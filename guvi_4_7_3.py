s = input()
d = dict()
l = len(s)
flag=True
max_len_local = 0
max_len_global = 0
for i in range(l):
    if ord(s[i])<97 or ord(s[i])>122:
        flag=False;break
    if s[i] in d:
        max_len_local = i-d[s[i]]
        d[s[i]]=i
    else:
        d[s[i]]=i
        max_len_local+=1
    max_len_global = max(max_len_global,max_len_local)
print(max_len_global) if flag else print('Invalid Input')