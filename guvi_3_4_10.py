def abcd(n):
    w = 0
    for i in str(n):
        w+=int(i)
    return str(w)==str(w)[::-1]
n = int(input())
if abcd(n):
    print('YES')
else:
    print('NO')