s=list(input());l=len(s)
if l%2==1:
    s[l//2]='*'
else:
    s[l//2]='*';s[l//2+1]='*'
print("".join(s))