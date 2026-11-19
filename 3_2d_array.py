import numpy  as np 

#create 2d array from 2d list
array_2d = np.array([[1,2,3],[4,5,6]])

print(array_2d)
print(f"Shape (row X column) = {array_2d.shape}")

#access 1st row and 1st column
print(array_2d[0][0]) # 1

#update 
array_2d[0][0] = 300
print(array_2d)