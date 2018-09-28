from os import *
for file in listdir("."):
    x=file.split('_')
    rename(file,x[0])
