# write a program to findout minimum and maximum value in tuple 
numbers = (12, 45, 7, 89, 23, 56, 91, 34, 18, 67, 5, 72, 39, 84, 26, 11, 95, 48, 63, 30)

min = numbers[0]
max = numbers[0]

for item in numbers:
    if item<min:
        min = item 
    if item>max:
        max = item 

print("minimum = ",min)
print("maximum = ",max)