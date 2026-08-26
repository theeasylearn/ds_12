# write a to findout given year is leap year or not 
year = int(input("Enter year"))
reminder1 = year % 4 
reminder2 = year % 100 
reminder3 = year % 400

if reminder1 == 0 and reminder2 !=0:
    print("this year is leap year")
else:
    if reminder2==0 and reminder3==0:
        print("this is leap year")
    else:
        print("this is not leap year")
