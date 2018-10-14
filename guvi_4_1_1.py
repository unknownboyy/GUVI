t=int(input())
s=[]
loopcunter=10**6
total_prefix_length=0
for i in range(t):
    s.append(input())
    loopcunter=min(loopcunter,len(s[-1]))
break_kar=False
mypre=""
for i in range(loopcunter):
    cur_ele=s[0][i]
    for j in range(1,t):
        if s[j][i]!=cur_ele:
            break_kar=True;break
    if break_kar:   break
    mypre=mypre+s[0][i]
print(mypre)
