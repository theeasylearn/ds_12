def calculation(num1,num2):
    #local variables 
    addition = num1 + num2 
    subtraction = num1 - num2 
    multiplication = num1 * num2
    division = num1 / num2 
    return addition,subtraction,multiplication,division

num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))

result = calculation(num1,num2) #here result is tuple and it will have 4 values (addition,subtraction,multiplication,division)

print(result)
print("addition = ",result[0])
print("subtraction = ",result[1])
print("multiplication = ",result[2])
print("division = ",result[3])

