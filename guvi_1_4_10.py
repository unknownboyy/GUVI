n=int(input())
fibo=[1,1]
for i in range(n-2):
    fibo.append(fibo[-1]+fibo[-2])
print(*fibo)