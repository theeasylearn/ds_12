import numpy as np 
#create 2d array 
arr = np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]],dtype=np.int8)
print(arr)

print("Dimension of array ",arr.ndim)
print("Shape (row X column)",arr.shape)
print("Data type of array ",arr.dtype)
print("Size of each value ",arr.itemsize)
print("Size of whole array  ",arr.nbytes)
print("Transposed array ")
print(arr.T)


