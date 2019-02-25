# from sys import argv
# print(argv)
def inc(s):
    length = 1
    local = 1
    for i in range(1,len(s)):
        if ord(s[i])>ord(s[i-1]):
            length+=1
        else:
            local = max(local,length)
            length = 1
    return max(local,length)
def dec(s):
    length = 1
    local = 1
    for i in range(1,len(s)):
        if ord(s[i])<ord(s[i-1]):
            length+=1
        else:
            local = max(local,length)
            length = 1
    return max(local,length)
s = input()
print(inc(s),dec(s))