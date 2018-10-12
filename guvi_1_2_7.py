n=input()
count=0
for i in n:
    count+=int(i)**3
print('yes') if count==int(n) else print('no')