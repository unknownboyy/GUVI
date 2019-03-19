def isTerminal(s):
  if (ord(s)>=97 and ord(s)<=122) or (ord(s)>=48 and ord(s)<=57):
    return True
  else:
    return False
n = int(input('Enter Number Of Productions'))
productions = []
for _ in range(n):
    productions.append(input('Enter Production'+str(_+1)))
d = dict()
for i in productions:
    left,right = i.split("=")
    right = right.split('|')
    rights = [list(i) for i in right]
    d[left] = rights
print(d)
string = input("Enter the string")
i = 0
current = 'S'
change=False
try:
        while i<len(string):
                print(current,'is current')
                current = d[current]
                print('curr',current)
                for functions in current:
                        print('functions',functions)
                        for letter in functions:
                                print('letter',letter)
                                if isTerminal(letter):
                                        if letter == string[i]:
                                                i+=1
                                        else:
                                                if isTerminal(letter):
                                                        change=False
                                                else:
                                                        change=True
                                                break
                                else:
                                        current = letter
                                        continue
                        if change:
                                current = letter
                                continue
except Exception as e:
        print(i,e)