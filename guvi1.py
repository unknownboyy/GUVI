def findSubarrays(arr, n): 
    found = False
    lsum = 0
    for i in range(n - 1): 
        lsum += arr[i] 
        rsum = 0
        for j in range(i + 1, n): 
            rsum += arr[j] 
        if (lsum * (n - i - 1) == rsum * (i + 1)): 
            found = True
    return found

n = int(input())
arr = list(map(int,input().split()))
print('yes') if findSubarrays(arr, n) else print('na')