# write a program to findout BMI (Body to mass index) of given weight and height 
#accept height
print("Enter your height (in feet and inch)")
foot = int(input("Enter only feet "))
inch = int(input("Enter only remaining inch"))
#accept weight
weight = float(input("enter your weight in kg"))

#process 
#calculate total inch
total_inch = (foot * 12) + inch

#convert centimeter 
meter = total_inch / 39.37

#calculate BMI 
bmi = weight / (meter * meter)

print(f"your BMI IS {bmi:.2f}")


