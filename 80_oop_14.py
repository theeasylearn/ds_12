import math 
#example of private variable
class Account:
    def __init__(self,name,acctype,balance):
        self.name = name 
        self.acctype = acctype
        self.__balance = balance 
        print("constructor called....")
    def display(self):
        print("-"*100)
        print("Name " + self.name)
        print("Balance " + str(self.__balance))
        print("Account Type " + self.acctype)
        print("-"*100)
    def updateBalance(self,amount):
        if amount < 0 and math.fabs(amount) > self.__balance:
            print("you are trying to withdraw more amount then amount in account, hence transaction is declined, sorry")
        elif amount>0:
            self.__balance += amount 
        else:
            self.__balance += amount

#create object 
a1 = Account("Ankit Patel","current",4500000)
a1.display()
a1.balance = 125000000 #ignore
a1.updateBalance(50000)
a1.display()

a1.updateBalance(-5050000)
a1.display()