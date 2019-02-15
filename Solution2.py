# QUE 7
# class Student:
#     def __init__(self, name, sec, course, marksObtained, maxMarks):
#         self.__name = name
#         self.__sec = sec
#         self.__course = course
#         self.__marksObtained = marksObtained
#         self.__maxMarks = maxMarks
#     def getName(self):
#         return self.__name
#     def getSec(self):
#         return self.__sec
#     def getCourse(self):
#         return self.__course
#     def getMaxMarks(self):
#         return self.__maxMarks
#     def getMarksObtained(self):
#         return self.__marksObtained
    
#     def setName(self, new_name):
#         self.__name = new_name
#     def setSec(self, new_sec):
#         self.__sec = new_sec
#     def setCourse(self, new_course):
#         self.__course = new_course
#     def setMaxMarks(self, new_marks):
#         self.__maxMarks = new_marks
#     def setMarksObtained(self, new_marks):
#         self.__marksObtained = new_marks
    
#     def getGrade(self):
#         p = self.__marksObtained/self.__maxMarks
#         if p>=0.9:  return 'A'
#         elif p>=0.8:    return 'B'
#         elif p>=0.7:    return 'C'
#         else: return 'D'

# QUE 8
# class Market:
#     def __init__(self, name, tax_dict, actual_price):
#         self.__name = name
#         self.__tax_dict = tax_dict
#         self.__actual_price = actual_price
    
#     def getName(self):
#         return self.__name
#     def getTaxDict(self):
#         return self.__tax_dict
#     def getActualPrice(self):
#         return self.__actual_price
#     def setName(self, new_name):
#         self.__name = new_name
#     def setTaxDict(self, new_tax_dict):
#         self.__tax_dict = new_tax_dict
#     def setActualPrice(self, new_price):
#         self.__actual_price = new_price
#     def addTax(self, tax_name, tax_amount):
#         self.__tax_dict[tax_name] = tax_amount
#     def haveTax(self, tax_name):
#         return tax_name in self.__tax_dict
#     def getFinalPrice(self):
#         final_tax = 0
#         for i in self.__tax_dict:
#             final_tax += self.__tax_dict[i]
#         return (1+0.01*final_tax)*self.__actual_price
    
# my_market = Market('pen',{"t1":6,"t2":7},6)
# my_market.addTax('tax1',5)
# my_market.addTax('tax1',27)
# print(my_market.haveTax('t3'))
# print(my_market.haveTax('t2'))
# print(my_market.getFinalPrice())

# QUE 1
# class Student:
#     def __init__(self, name, sec, course, marksObtained, maxMarks):
#         self.__name = name
#         self.__sec = sec
#         self.__course = course
#         self.__marksObtained = marksObtained
#         self.__maxMarks = maxMarks
#     def getName(self):
#         return self.__name
#     def getSec(self):
#         return self.__sec
#     def getCourse(self):
#         return self.__course
#     def getMaxMarks(self):
#         return self.__maxMarks
#     def getMarksObtained(self):
#         return self.__marksObtained
    
#     def setName(self, new_name):
#         self.__name = new_name
#     def setSec(self, new_sec):
#         self.__sec = new_sec
#     def setCourse(self, new_course):
#         self.__course = new_course
#     def setMaxMarks(self, new_marks):
#         self.__maxMarks = new_marks
#     def setMarksObtained(self, new_marks):
#         self.__marksObtained = new_marks
    
#     def getGrade(self):
#         p = self.__marksObtained/self.__maxMarks
#         if p>=0.9:  return 'A'
#         elif p>=0.8:    return 'B'
#         elif p>=0.7:    return 'C'
#         else: return 'D'

#     def __str__(self):
#         return self.__name + '_' + self.getGrade()

# filename = 'students.txt'
# n = int(input())
# file = open(filename,'w')
# for i in range(n):
#     x = input().split()
#     new_student = Student(x[0],x[1],x[2],float(x[3]),float(x[4]))
#     file.write(str(new_student)+'\n')
# file.close()

# file = open(filename,'r')
# flag=False
# x=input()
# for i in file:
#     if i.split('_')[0] == x:
#         print(x,'Have Grade',i.split('_')[1])
#         flag=True
# if not flag:
#     print('Student Not Found')

# QUE 2 (use try except wherever there is a possibility of error (i.e., check file/use try except))

# QUE 3
# import os
# n =int(input())
# count = 0
# for i in range(n):
#     file = input()
#     if os.path.isfile(file):
#         count+=1
# print('Total',count,'File Exists')

# QUE 4
# def binToDecimal(string,power=0):
#     if len(string) == 1:
#         return 2**power*int(string)
#     else:
#         return 2**power*(ord(string[-1])-ord('0')) + binToDecimal(string[:-1],power+1)
# print(binToDecimal('110'))

# QUE 5
# def binToDecimal(string,power=0):
#     if len(string) == 1:
#         return 2**power*int(string)
#     else:
#         return 2**power*(ord(string[-1])-ord('0')) + binToDecimal(string[:-1],power+1)
# def hexa(x):
#     if x == 0:
#         return ''
#     else:
#         w = x % 16
#         if w>=10:
#             w=chr(ord('A')+(w-10))
#         else:
#             w=str(w)
#         return hexa(x//16)+w
# x = input()
# x = binToDecimal(x)
# print(hexa(x))

# QUE 6
# n = int(input())
# c= 0
# for i in range(32):
#     if n & (1<<i):
#         c += 1
# print('YES') if c%2==0 else print('NO')

# END OF Solution