s = list(input())
signchange = False
w = []
for i in range(len(s)):
    if s[i] not in ['(',')','+','-']:
        w+=s[i]
    elif s[i] in ['+','-']:
        if signchange:
            if s[i]=='-':
                s[i]='+'
            else:
                s[i]='-'
        if i<len(s)-1 and s[i+1]=='(' and s[i]=='-':
            signchange=True
        w+=s[i]
    elif signchange and s[i]==')':
        signchange=not(signchange)
print("".join(w))