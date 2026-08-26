#example of recursion 
# write a program to print 1 to 100
def printNumber(num): #2
    if num<=100:
        print(num,end=' ') #
        num = num + 1 #3
        printNumber(num) #recursion
num = 1
printNumber(num)
