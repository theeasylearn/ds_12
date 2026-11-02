# write a program to calculate strike rate of batter using given runs and balls 
try:
    runs = int(input("Enter Runs scored by batter"))
    balls = int(input("Enter balls played by batter"))
    strike_rate = (runs / balls) * 100
except ZeroDivisionError:
    print("invalid input: Balls must not be zero")
except ValueError:
    print("invalid input type : ball and runs must be integer")
else: 
    print(f"Strike rate = {round(strike_rate,2)}")
finally:
    print("Thank you for using our program.")



