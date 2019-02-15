class Account:
    def __init__(self,id=0,balance=100,annualInterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
    
    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setId(self,new_id):
        self.__id = new_id

    def setBalance(self,new_balance):
        self.__balance = new_balance

    def setAnnualInterestRate(self,new_interest):
        self.__annualInterestRate = new_interest
    
    def getMonthlyInterestRate(self):
        return self.__annualInterestRate/12
    
    def getMonthlyInterest(self):
        return (self.__annualInterestRate*self.__balance)/1200
    
    def withdraw(self,amount):
        self.__balance -= amount
    
    def deposit(self,amount):
        self.__balance += amount

#Test Program Starts Here...
my_input = list(map(float,input().split()))
myaccount = Account(my_input[0],my_input[1],my_input[2])
x,y=input().split()
if x=='W':
    myaccount.withdraw(float(y))
else:
    myaccount.deposit(float(y))
x,y=input().split()
if x=='W':
    myaccount.withdraw(float(y))
else:
    myaccount.deposit(float(y))
print(myaccount.getId(,myaccount.getBalance(),myaccount.getMonthlyInterestRate(),myaccount.getMonthlyInterest()))