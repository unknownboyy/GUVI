for i in range(10):
    filename = 'guvi_4_3_'+str(i+1)+'.py'
    file = open(filename,"w")
    file.write('print('+filename+')')
    file.close()