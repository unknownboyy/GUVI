f=[1,1,2]
for i in range(3,91):
    f.append(f[-1]+f[-2])
for target_list in range(int(input())) :
    n=int(input())
    print(f[n])