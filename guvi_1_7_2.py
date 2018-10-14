zeroones=0
s=input()
for i in s:
    if i=='0' or i=='1':
        zeroones+=1
print('yes') if len(s)==zeroones else print('no')