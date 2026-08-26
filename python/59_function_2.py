#default argument function 
def getSeconds(hours,minutes=0,seconds=0):
    #this function will return total seconds of given hour, minutes, seconds 
    totalSecond = hours * 3600
    totalSecond = totalSecond + (minutes * 60)
    totalSecond = totalSecond + seconds
    return totalSecond

hours = int(input("Enter hours"))   
minutes = int(input("Enter minutes"))
seconds = int(input("Enter seconds"))

totalSeconds = getSeconds(hours,minutes,seconds)
print("Total seconds using hours, minutes and seconds ",totalSeconds)

totalSeconds = getSeconds(hours,minutes)
print("Total seconds using hours, minutes ",totalSeconds)

totalSeconds = getSeconds(hours)
print("Total seconds using hours ",totalSeconds)