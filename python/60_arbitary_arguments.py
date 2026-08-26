# concept of arbitrary(argument are not fixed it can be range from 1 to N) argument function in python 
def getMax(*numbers):
    #local variable 
    max = numbers[0] #10
    for num in numbers: #20
        if num>max: #40>30
            max = num  #40
    return max  

max = getMax(100,500,50,1000,500,5000,11000,7500)
print(max)
