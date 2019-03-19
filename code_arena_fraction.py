def check(n):
    count = 0
    for i in str(n):
        count+=int(i)
    if str(count)[0]=='1':
        return count
    else:
        return False
n = int(input())
l = [8]
c = 0
diff = 2
curr = 800
while curr+diff<=n:
    curr+=diff
    w = check(curr)
    if w!=False:
        l.append(w)
    diff+=2
    c+=1
print(*l)
print(c)