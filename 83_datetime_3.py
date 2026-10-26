# compare dates 
# write a program to findout who is elder person between husband and wife 
from datetime import datetime as dt 
husband_birth_date = input("Enter husband birthdate (dd-mm-YY)")
husband_birth_date  = dt.strptime(husband_birth_date,"%d/%m/%Y")

wife_birth_date = input("Enter wife birthdate (dd-mm-YY)")
wife_birth_date  = dt.strptime(wife_birth_date,"%d/%m/%Y")

if husband_birth_date<wife_birth_date:
    print("Husband is elder person")
else:
    print("wife is elder person")

print("Husband birth date is ",dt.strftime(husband_birth_date,"%m-%d-%Y"))
print("wife birth date is ",dt.strftime(wife_birth_date,"%d-%m-%Y"))


