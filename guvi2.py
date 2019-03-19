import re
string = input()
pattern = re.compile(r'^[\w]{3,}@[\w]{4,}.com$')
print('YES') if pattern.match(string) else print('NO')