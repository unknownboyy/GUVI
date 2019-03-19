for _ in open('testcases2.txt','r').readlines():
    in_file = open(_[:len(_)-1]+'.txt','r')
    data = in_file.readlines()
    in_file.close()
    pics = int(data.pop(0).strip())
    pic_list = []
    horizontals = []
    verticals = []
    for i in range(pics):
        line = list(data.pop(0).strip().split())
        orientation = line[0]
        ntags = int(line[1])
        tags = set(line[2:])
        if orientation=='H':
            horizontals.append([orientation,ntags,tags,[i]])
        else:
            verticals.append([orientation,ntags,tags,[i]])
    pic_list = horizontals
    verticals.sort(key=lambda x:x[1],reverse=True)
    for i in range(0,len(verticals)-1,2):
        pic_list.append(['V',verticals[i][1]+verticals[i+1][1],verticals[i][2]|verticals[i+1][2],verticals[i][3]+verticals[i+1][3]])
    pics = len(pic_list)
    alloted = [-1]*pics
    loop = True
    i = 0
    slideshow = [[0,0]]
    while loop:
        print(i)
        alloted[i]=i
        find_index = -1
        min_value = 0
        for j in range(pics):
            if alloted[j]==-1:
                a = pic_list[i][2]
                b = pic_list[j][2]
                if min_value < max(min_value,min( len(a&b) , len(a-b) , len(b-a) )):
                    min_value = max(min_value,min( len(a&b) , len(a-b) , len(b-a) ))
                    find_index = j
        alloted[i]=find_index
        i = find_index
        if find_index==-1:
            loop=False
        else:
            slideshow.append([i,min_value])
            output = open(_[:len(_)-1]+'_out.txt',"a")
            output.write(str(i)+"\n")
            output.close()
    # output = open(_[:len(_)-1]+'_out.txt',"w")
    # for i in slideshow:
    #    output.write(" ".join(list(map(str,pic_list[i[0]][3])))+"\n")
    #output.close()