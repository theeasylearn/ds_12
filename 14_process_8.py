# write a program to findout B.M.I. (Body to mass index) of given weight and height 
#accept input
weight = float(input("Enter weight in KG"))
print("Enter your height in foot and inches")
feet = int(input("Enter only feet"))
inch = int(input("Enter only remaining inches"))

# process 
# calculate total inch 
total_inch = (feet * 12) + inch 

#convert total inch into meter 
meter = total_inch / 39.37 

#calculate BMI 
bmi = weight / (meter * meter)
print(f"your bmi is {bmi:.2f}")

