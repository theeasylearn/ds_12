# write a program to findout annual income from given monthly income and also calculate and display 20% tax on it and calculate display net income 
monthly_income = int(input("Enter monthly income"))

#process
#variable-name = variable-name symbol variable-name/value
annual_income = monthly_income * 12

#calculate 20% tax 
tax = (annual_income * 20) / 100

#net income 
net_income = annual_income - tax 

#display all variables
print("Annual income ",annual_income)
print("tax = ",tax)
print("Net income",net_income)