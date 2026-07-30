#example of user defined function 
def getSquare(num):
    #create local variable square
    square = num * num 
    return square 

number = int(input("Enter number"))
#calculate square 
result = getSquare(number) #use, execute, call 
print(result)

