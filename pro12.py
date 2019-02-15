for _ in range(int(input())):
    s = input()
    l = len(s)
    w = [0]*26
    for i in s:
        w[ord(i)-65]+=1
    w.sort(reverse=True)
    answer = 10**6
    for i in range(26):
        if l%(i+1)==0:
            should = l//(i+1)
            count = 0
            for j in range(i+1):
                count+=max(0,w[j]-should)
            count+=sum(w[i+1:])
            answer = min(answer,count)
    print(answer)
