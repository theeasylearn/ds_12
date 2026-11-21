import numpy as np 

np.random.seed(42)
#create 2d float array size 3 x 4
arr = np.random.rand(3,4)
print(arr)
#create integer array size 3 x 4
arr = np.random.randint(1,10,5)
print(arr)

arr = np.random.uniform(1,5,3)
print(arr)

fruits = ['apple','banana','mango','pinapple','watermelon']
print(fruits)
print("Pick any one random fruit",np.random.choice(fruits))
# shuffle list 
np.random.shuffle(fruits)
print(fruits)