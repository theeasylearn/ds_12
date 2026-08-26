class MyMath:
    #constructor 
    def __init__(self,a,b):
        #create instance variables
        self.num1 = a
        self.num2 = b
        print("constructor called....")
    def getAddition(self):
        #create local variable 
        result = self.num1 + self.num2 
        return result 
    def getSubtraction(self):
        result = self.num1 - self.num2 
        return result 
#task 
# add 2 more method getMultiplication and getDivision
#create object
num1 = int(input("Enter num 1"))
num2 = int(input("Enter num 2"))

m1 = MyMath(num1,num2) #it will run constructor automatically 
result = m1.getAddition()
print("result of addition = ",result)

result = m1.getSubtraction()
print("result of subtraction = ",result)


m2 = MyMath(1000,200)
result = m2.getAddition()
print("result of addition = ",result)


result = m2.getSubtraction()
print("result of subtraction = ",result)
