# Section A
# QUE 1
# from math import tan,pi
# n,s=map(float,input().split())
# print('Area = ',(n*s**2)/(4*tan(pi/n)))

# QUE 2
# w1,p1 = map(float,input().split())
# w2,p2 = map(float,input().split())
# if w1/p1<w2/p1:
#     print('Price 1 is better')
# else:
#     print('Price 2 is better')

# QUE 3
# x,y = map(float,input().split())
# if x<5 and x>-5 and y<2.5 and y>-2.5:
#     print('Inside')
# else:
#     print('Outside')

# QUE 4
# p=[True]*1000
# for i in range(2,int(1000**0.5)+2):
#     if p[i]:
#         for j in range(i+i,1000,i):
#             p[j]=False
# for i in range(2,1000-2):
#     if p[i] and p[i+2]:
#         print('('+str(i)+','+str(i+2)+')')

# QUE 5
# num = input()
# checksum = 0
# for i in range(12):
#     if i%2==0:
#         checksum+=(ord(num[i])-ord('0'))
#     else:
#         checksum+=3*(ord(num[i])-ord('0'))
# checksum = 10-(checksum%10)
# if checksum==10:
#     checksum=0
# print(num+str(checksum))

# Section B
# QUE 1
# s1=" HELLO world ";s2=" Hello "
# substring1 = s1[1:4+1]
# s3 = s1.lower()
# s3 = s1.upper()
# s3 = s1.strip()
# s1.replace('e','E')

# QUE 2
# Anagram
# def is_anagram(s1,s2):
#     c1=[0]*26;c2=[0]*26;s1=s1.lower();s2=s2.lower()
#     for i in s1:    c1[ord(i)-97]+=1
#     for i in s2:    c2[ord(i)-97]+=1
#     for i in range(26):
#         if c1[i]!=c2[i]:    return False
#     return True
# print(is_anagram("Hello","hello"))

# Rotate Pairs
# word = list(input())
# wordList = []
# for i in range(len(word)):
#     wordList.append("".join(word))
#     word.append(word.pop(0))
# print(*wordList)

# QUE 3
# Happiness Calc
# n = int(input())
# a,b=map(int,input().split())
# arr = list(map(int,input().split()))
# A = set(map(int,input().split()))
# B = set(map(int,input().split()))
# happiness = 0
# for i in arr:
#     if i in A:
#         happiness+=1
#     if i in B:
#         happiness-=1
# print(happiness)

# User-defined Exception
# class Error(Exception):
#     def __init__(self,msg):
#         self.__msg = msg
#     def __str__(self):
#         return self.__msg
# n=int(input())
# try:
#     raise Error("Gaurang Error")
# except Error as Gaurang:
#     print(Gaurang)

# Section C
# QUE 1
# Time
# class Time:
#     def __init__(self, hour, minute, second):
#         self.__second = second
#         self.__minute = minute
#         self.__hour = hour
    
#     def getHours(self):
#         return self.__hour

#     def getMinutes(self):
#         return self.__minute
    
#     def getSeconds(self):
#         return self.__second
    
#     def setTime(self, new_seconds):
#         self.__hour = new_seconds//3600
#         new_seconds = new_seconds%3600
#         self.__minute = new_seconds//60
#         new_seconds = new_seconds%60
#         self.__second = new_seconds

# myTime = Time(10,20,30)
# elapsedTime = int(input("Enter Time to be elapsed"))
# myTime.setTime(elapsedTime)
# print(myTime.getHours(),myTime.getMinutes(),myTime.getSeconds())

# Location
# class Location:
#     def __init__(self, row, column, maxValue):
#         self.row = row
#         self.column = column
#         self.maxValue = maxValue
    
# def locateLargest(a):
#     i_ind = 0
#     j_ind = 0
#     maxValue = a[0][0]
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             if a[i][j]>maxValue:
#                 maxValue = a[i][j]
#                 i_ind = i
#                 j_ind = j
#     return Location(i_ind,j_ind,maxValue)

# m,n=map(int,input('Enter Rows And Columns of matrix').split())
# matrix=[]
# for i in range(n):
#     matrix.append(list(map(int,input().split())))
# largest_location = locateLargest(matrix)
# print(largest_location.row,largest_location.column,largest_location.maxValue)

# QUE 2
# Random Integers In File
# import os
# import random
# myfile = input('Enter File Name')
# if os.path.isfile(myfile):
#     print('File Already Exists')
# else:
#     my_new_int_list = [random.randint(0,1000) for i in range(100)]
#     my_new_str_list = list(map(str,my_new_int_list))
#     file = open(myfile,'w')
#     data = " ".join(my_new_str_list)
#     file.write(data)
#     file.close()

#     file = open(myfile,'r')
#     dataList = list(map(int,file.readline().split(' ')))
#     dataList.sort()
#     print(*dataList)
#     file.close()

# Longest Length Word in File
# import os
# file_name = input('Enter File Name')
# if os.path.isfile(file_name):
#     file = open(file_name,'r')
#     max_length = 0
#     max_length_word = ''
#     for i in file:
#         for j in i:
#             if len(j)>max_length:
#                 max_length = len(j)
#                 max_length_word = j
#     print('Max Length Word=',max_length_word)
# else:
#     print('File Not Exists')

# QUE 3
# Method 1 (Manual Calculation Method)
# locker = [False]*100
# for i in range(1,100+1):
#     for j in range(i,100+1,i):
#         locker[j-1]=not locker[j-1]
# open_lockers = []
# for i in range(100):
#     if locker[i]:
#         open_lockers.append(i+1)
# print('Open Lockers',*open_lockers)

# Method 2 (Print All Semi-Primes Till 100) => Print All Perfect_Squares
# i=1
# open_lockers = []
# while i*i<=100:
#     open_lockers.append(i*i)
#     i+=1
# print('Open Lockers',*open_lockers)


# END OF SAMPLE PAPER