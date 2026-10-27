# how to get current date and time 
from datetime import datetime as dt 

#create datetime class object
current = dt.now()

#current date 
week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
print(week[current.weekday()] + " " + str(current.day) + "/" + str(current.month) + "/" + str(current.year))

# current time 
time = str(current.hour) + ":" + str(current.minute)
print(time)


