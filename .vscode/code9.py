def func():
    pass

n = int(input())
productions = []
for _ in range(n):
    productions.append(input())
functions = []
for i in productions:
    left,right = i.split("=")
    right = right.split('|')
    functions.append([left,right])
print(functions)