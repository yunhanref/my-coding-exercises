import numpy as np
array_to_analyse = np.random.randint(10,100,(3,3))
print(array_to_analyse.shape) #output = (column,row) (3,3)
print(array_to_analyse.ndim) #output =  2 (Dimensions)
print(array_to_analyse.size) #output = row*column = 3*3 = 9 elements
print(array_to_analyse.dtype) #output = int64 (the array has integer values)
