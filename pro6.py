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
    while freq[-1]==0:
        freq.pop()
    #print(*freq)
    change = len(s)
    for i in range(len(freq)):
        if l%(i+1)==0:
            local = 0
            for j in range(min(i,len(freq))):
                if freq[j]>0:
                    local += (freq[j]-1)*(j+1)
            for j in range(i+1,len(freq)):
                if freq[j]>0:
                    local += (j-i)*freq[j]
            change = min(change,local)
    print(change)