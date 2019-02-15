<<<<<<< HEAD
for _ in range(int(input())):
    s = input()
    l = len(s)
    arr = [0]*26
    for i in s:
        arr[ord(i)-65]+=1
    arr.sort()
    freq = [0]*(len(s)+1)
    for i in arr:
        freq[i]+=1
    freq.pop(0)
    print(*freq)
    change = len(s)
    for i in range(len(freq)):
        if l%(i+1)==0:
            times = l//(i+1) - freq[i]
            local = 0

            for j in range(i+1,len(freq)):
                if freq[j]>0:
                    local += (j-i)*freq[j]
                    times-=1
            
            for j in range(min(i,len(freq))-1,-1,-1):
                if freq[j]>0:
                    if times>0:
                        local += (freq[j]-1)*(j+1)
                        times-=1
                    else:
                        local += freq[j]*(j+1)

            change = min(change,local)
    print(change)

# 1
# ABCABCABCABCDEF
# 3 0 0 3 0 0 0 0 0 0 0 0 0 0 0
# 5
=======
def solve(s,n):
    i=0
    while i<n and s[i]=='#':
        i+=1
    ind=i
    for i in range(ind,n-1):
        if s[i]=='#' and s[i+1]=='#':
            return False
    q=s[ind:].count('#')
    count=0
    while ind<n and q>0:
        if s[ind]=='.':
            count+=q
        else:
            q-=1
        ind+=1
    return count
for _ in range(int(input())):
    n=int(input())
    s=list(input())
    x=solve(s,n)
    if x:
        print(x)
    else:
        print(-1)
>>>>>>> 33f4cd762d4e4b8b825025741676af85251a142b
