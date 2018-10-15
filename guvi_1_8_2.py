vowels='aeiouAEIOU'
flag=False
for i in input():
    if i in vowels:
        flag=True
print('yes') if flag else print('no')