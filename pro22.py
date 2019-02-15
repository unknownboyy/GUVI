# Balanced Parenthesis

st = []


def calc(string):
    st=[]
    for i in string:
        if i == '(':
            st.append(i)
        elif i =='{':
            st.append(i)
        elif i == '[':
            st.append(i)
        elif i == ')':
            try:
                if st[-1]!='(':
                    raise RuntimeError
                else:
                    st.pop()
            except:
                return False
        
        elif i == '}':
            try:
                if st[-1]!='{':
                    raise RuntimeError
                else:
                    st.pop()
            except:
                return False
        elif i == ']':
            try:
                if st[-1]!='[':
                    raise RuntimeError
                else:
                    st.pop()
            except:
                return False
    
    return len(st)==0

def braces(values):
    ans = []
    for i in values:
        if calc(i):
            ans.append('YES')
        else:
            ans.append('NO')
    return ans

    
n = int(input())
l = []
for i in range(n):
    l.append(input())
print(*braces(l),sep='\n')