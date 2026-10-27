# compare dates 
# write a program to findout who is elder person between husband and wife 
import datetime as dt 
print("Enter husband birth detail")
day = int(input("Enter day of birth"))
month = int(input("Enter month of day"))
year = int(input("Enter year of the day"))

#create date object 
husband_birth_date  = dt.date(year,month,day)

print("Enter wife birth detail")
day = int(input("Enter day of birth"))
month = int(input("Enter month of day"))
year = int(input("Enter year of the day"))

wife_birth_date  = dt.date(year,month,day)

if husband_birth_date<wife_birth_date:
    print("Husband is elder person")
else:
    print("wife is elder person")




