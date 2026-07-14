# write a program to accept day of week from user and print name of day of week 

day = int(input("Enter day of week"))

if day == 1:
    print("it is monday")
elif day == 2:
    print("it is tuesday")
elif day == 3:
    print("it is wednesday")
elif day == 4:
    print("it is thursday")
elif day == 5:
    print("it is is friday")
elif day == 6:
    print("it is saturday")
elif day == 7:
    print('it is sunday')
else:
    print('it is not valid day')