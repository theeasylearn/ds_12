import numpy as np 

array_1 = np.array([10,20,30,40,50])

# array_2 = array_1 wrong way of copying array 

array_2 = array_1.copy()

print(array_1)
print(array_2)

array_1[0] = 1000
array_2[1] = 2000
print(array_1)
print(array_2)
