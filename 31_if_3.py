#write a to convert 24 hours format time into 12 hours format time and display it 
# input: 23 output : 11 PM
# input: 13 output : 1 PM
# input: 14 output : 2 PM
# input: 07 output : 7 AM

hours = int(input("Enter hours"))
if hours<=12:
    print(f"{hours} A.M.")

if hours>12:
    # hours = hours - 12 
    hours-=12
    print(f"{hours} P.M.")

print("Good bye")

