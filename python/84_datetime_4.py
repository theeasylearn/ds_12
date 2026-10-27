# add days into date 
# write a program to findout who is elder person between husband and wife 
from datetime import datetime as dt 
from datetime import timedelta 
recharge_date = input("Enter recharge date (dd/mm/yyyy)")
days = int(input("Enter recharge days "))

recharge_date = dt.strptime(recharge_date,"%d/%m/%Y")
#add no of days into date object
recharge_expiry_date = recharge_date.__add__(timedelta(days=days))
print("Your recharge will expire on ",dt.strftime(recharge_expiry_date,"%d/%m/%Y"))
