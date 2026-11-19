import numpy as np 

#create list 
list = [10,20,30,40,50]

#create tuple 
tuple = (1,2,3,4,5.99)

#create array using list 
a = np.array(list)

#create array using tuple 
b = np.array(tuple)

print(a)
print(b)

#access 1st value
print(a[0])

#update value 
a[0] = 100
print(a)

