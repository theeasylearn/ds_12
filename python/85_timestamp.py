#getting time stamp

from datetime import datetime as dt 

timestamp = dt.now().timestamp()
print(int(timestamp))

#add 10 days 
seconds = 60 * 60 * 24 * 10
timestamp = int(timestamp) + seconds

#convert timestamp into datetime 
tomorrow = dt.fromtimestamp(timestamp)
print(tomorrow)