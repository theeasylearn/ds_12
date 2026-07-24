# write a program to calculate and display compound interest of given amount, rate, year 
amount = int(input("Enter amount"))
rate = float(input("Enter rate"))
year = int(input("Enter year"))
original_amount = amount 
while year>0:
    interest = (amount * rate * 1) / 100
    amount = amount + interest 
    year = year - 1
amount = amount - original_amount
print(f"compound interest = {amount:.2f}")