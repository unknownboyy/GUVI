import random
li=[]
for i in range(100):
    li.append(random.randint(1,99))
s=set()
for i in li:
    s.add(i)
if len(s)==99:
    print('Contains All Elements')
else:
    print('Sorry...!!\nSome Elements Are Missing...')