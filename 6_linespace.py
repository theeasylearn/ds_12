import numpy as np 

#create array which has 10 value between 1 and 2 
array_1 = np.linspace(1.0,2.0,num=10)
print(array_1)

#create array which has 10 value between 1 and 2 (not including)
array_2 = np.linspace(1.0,2.0,num=10,endpoint=False)
print(array_2)

#create array which has 10 value between 1 and 3 (not including) but return step size
array_3, step  = np.linspace(1.0,3.0,num=10,endpoint=False,retstep=True)
print(array_3)
print(f"Step size = {step}")

