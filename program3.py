for i in range(10):
    filename = 'guvi_4_2_'+str(i+1)+'.py'
    file = open(filename,"w")
    file.write('print("'+filename+'")')
    file.close()