'''
from time import time
from random import shuffle
my_list = [x for x in range(1000000)]
my_set = set(my_list)
ele = my_list.copy()
shuffle(ele)
st=int(time()*1000)
for element in ele:
    element in my_set
fi=int(time()*1000)
running_time = fi - st
print('Time to find',len(ele),'elements in set is',running_time,'milliseconds')

st=int(time()*1000)
for element in ele:
    element in my_list
fi=int(time()*1000)
running_time = fi - st
print('Time to find',len(ele),'elements in list is',running_time,'milliseconds')
'''

