#debugging 
#example of user defined function 

#without return value without argument function
def printLine():
    print("-"*100)

#with return value without argument function 
def getPI():
    #create local variable 
    pi = 22/7
    return pi

#without return value with argument function 
def printLetter(letter,count):
    print(letter*count)

#with return value with argument(input) function
def getSquare(num):
    #create local variable square
    square = num * num 
    return square 

def getCube(num):
    #create local variable cube
    cube = num * num * num 
    return cube 

printLine() #first time
number = int(input("Enter number"))
#calculate square 
printLetter('*',110)
result = getSquare(number) #use, execute, call, run  
print("Square = ",result)
printLine() #third time

result = getCube(number) #use, execute, call, run
print("Cube = ",result)
printLetter('!',25) 

radius = int(input("Enter radius"))

# square = getSquare(radius)
# pi = getPI(); #3.14
# area = pi * square # 10000
area = getPI() * getSquare(radius)
printLetter("$",100)
print("Area of circle ",area)