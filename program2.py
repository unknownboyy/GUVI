def func(money,arr):
    c = [0]*(money+1);c[0] = 1
    for i in range(len(arr)):
        for j in range(1,money+1):
            if j>=arr[i]:
                c[j]+=c[j-arr[i]]
                print('For Coin',arr[i],'For Amount',j,'Array :',*c)
    return c[money]
print(func(12,[1,2,5]))