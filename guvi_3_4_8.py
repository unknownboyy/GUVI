l = []
def func(rem,s,left,right):
    if rem<=0:
        if left==right:
            l.append(s)
    else:
            func(rem-1,s+"{",left+1,right)
            if right<left:
                func(rem-1,s+"}",left,right+1)
n = int(input())
func(2*n-1,"{",1,0)
print(*l,sep='\n')