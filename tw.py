class Error(Exception):
    def __init__(self,msg):
        self.__msg = msg
    def __str__(self):
        return self.__msg
n=int(input())
try:
    raise Error("Gaurang Error")
except Error as Gaurang:
    print(Gaurang)
