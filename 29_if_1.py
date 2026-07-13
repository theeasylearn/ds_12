#write a program to accept 2 brothers age from user. findout and display who is elder brother 
age1 = int(input("Enter 1st brother age"))
age2 = int(input("Enter 2nd brother age"))

if age1>age2: # == != < <= > >=
    print("1st brother is elder brother")

if age1<age2: # == != < <= > >=
    print("2nd brother is elder brother")

if age1==age2:
    print("both brother's age is same")

print("Good bye")