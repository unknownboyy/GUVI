a=[]
b=[]
c=[]
d=[]
e=[]
for i in range(1,32):
    if i&1: a.append(i)
    if i&2: b.append(i)
    if i&4: c.append(i)
    if i&8: d.append(i)
    if i&16:    e.append(i)
val=''
print('Lets play a game \nThink of a number')
print('Note: Give answer in 1/0')
print(*a)
s=input('Your no. is here?')
val+=s
print(*b)
s=input('Your no. is here?')
val+=s
print(*c)
s=input('Your no. is here?')
val+=s
print(*d)
s=input('Your no. is here?')
val+=s
print(*e)
s=input('Your no. is here?')
val+=s
print('Your Birthdate is: ',int(val[::-1],2))

