# write a program to convert decimal number into binary number 
def binary(num):
    if num>0:
        reminder = num % 2
        num = num // 2 
        binary(num) #recursion 
        print(reminder,end=' ')
num = int(input("Enter number"))
binary(num)

