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
