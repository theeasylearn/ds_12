#write a program to findout which farm is bigger in area from 2 given farms' length and width

print("Enter 1st farm area")
length1 = int(input("Enter 1st farm length"))
width1 = int(input("Enter 1st farm width"))

print("Enter 2nd farm area")
length2 = int(input("Enter 2nd farm length"))
width2 = int(input("Enter 2nd farm width"))

#calculate area 
area1 = length1 * width1
area2 = length2 * width2

#compare area 
if area1>area2:
    print("1st farm is bigger then 2nd farm")
else:
    print("2nd farm is bigger then 1st farm")

print("good bye")
