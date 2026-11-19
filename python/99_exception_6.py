#example of custom exception 
# write a program to accept runs scored by batter on each ball he played. calculate and display total ball & ball played and strike rate as well as make sure batter can score more then 6 run in ball.
#create custom exception using class
class TooManyRuns(Exception):
    pass 

runs = [] 
balls = 0
while True:
    try:
        run = int(input("Enter run betwen 0 to 6 (-1 to stop)"))
        if run>6:
            raise TooManyRuns("batter can not score more then 6 run")
        balls+=1 
        if run == -1:
            print("Batter is out")
            break
        runs.append(run)
    except TooManyRuns as error:
        print(error)
    except ValueError:
        print("it is not valid run.")
        
print("total run scored by batter ",sum(runs)," Balls played ",balls, "Strike rate ",(sum(runs)/balls)*100)
