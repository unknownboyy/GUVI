from collections import OrderedDict
d=OrderedDict()
for i in input():
    d[i]+=1
for i in sorted(d.keys()):
    print(i,d[i])