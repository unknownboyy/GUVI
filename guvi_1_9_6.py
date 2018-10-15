my_dictionary_to_keep_track=dict()
x,y=input().split()
if len(x)!=len(y):
    print('no')
else:
    flag=True
    for i in range(len(x)):
        if x[i] in my_dictionary_to_keep_track and my_dictionary_to_keep_track[x[i]]!=y[i]: flag=False;break
        else:
            my_dictionary_to_keep_track[x[i]]=y[i]
    if flag:    print('yes')
    else:
        print('no')