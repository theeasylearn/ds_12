#write a program to print multiplication table of given number
# number = 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
number = int(input("Enter number"))
for multiplier in range(1,11):
    print(f"{number} X {multiplier} = {number*multiplier}")