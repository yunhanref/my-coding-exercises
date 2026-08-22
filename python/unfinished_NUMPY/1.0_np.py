import numpy as np
### This is the re inspection of my numpy skills

## ARRAY CREATION
# Common Array Creation
manual_1Darray = np.array([1,2,3]) # created 1 dimensional [1,2,3] numpy list
manual_2Darray = np.array([(1,2,3),(4,5,6),(7,8,9)]) # created 2 dimensional [1,2,3],[4,5,6],[7,8,9] numpy matrix
loop_1Darray = np.array([i for i in range(4)]) # created 1 dimensional ([0, 1, 2, 3]) numpy list
loop_2Darray = np.array([(i for i in range(1,4)),(i for i in range(4,7)),(i for i in range(7,10))]) # created 2 dimensional [1,2,3],[4,5,6],[7,8,9] numpy matrix #!WHY DOES IT PRINT OBJECTS INSTEAD OF VALUES?
# Built in Special Arrays
zeros = np.zeros((2,2)) # creates 2 by 2 zeros matrix
ones = np.ones((2,2)) # creates 2 by 2 ones matrix
full = np.full((2,2),19) # creates 2 by 2 19 values matrix
identity1 = np.eye(3) # creates 3 by 3 identity matrix
identity2 = np.identity(3) # creates 3 by 3 identity matrix
arange = np.arange(2,11,2) # counts 2 by 2 from includedStart(2) to excludedEnd(11)
linspace1 = np.linspace(0,1,10,endpoint=False) #output = ([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
linspace2 = np.linspace(0,1,10,endpoint=True) #output = ([0., 0.11111111, 0.22222222, 0.33333333, 0.44444444,0.55555556, 0.66666667, 0.77777778, 0.88888889, 1])
randint = np.random.randint(10,100,(2,2)) #creates 2 by 2 matrix with values between 10 and 100
random = np.random.random((2,2)) #creates 2 by 2 matrix with values between 0 and 1

## SHAPE and DIMENSION OPERATIONS
# Array Info
array = np.eye(3)
array.shape #prints (column count, rows count). #Output is: (3,3)
array.ndim #prints the dimension (1dim = list, 2dim = matrix etc.). #Output is: 2
array.dtype #prints the datatype of the array. #Output is: dtype('int64')
array.size #prints the result of rows*columns. #Output is: 3*3 = 9
# Array Manipulation
reshaped_array1 = array.reshape((1,array.size)) #reshapes the size if possible.
reshaped_array2 = array.reshape((array.size,1)) #reshapes the size if possible.
flatten = array.flatten() # turns the multidimensional array to 1d vector.
ravel = array.ravel() # turns the multidimensional array to 1d vector.
#! np.squeeze() #LEARN LATER!
#! np.expand_dims() #LEARN LATER!
#! np.swapaxes() #LEARN LATER!

## MATH OPERATIONS ON NUMPY ARRAYS
array2 =  np.array([(1,2,3),(10,20,30),(100,200,300)])
sum_total = np.sum(array,axis=None,dtype=float) #Sums all values of the array and prints. Output is: np.int64(sum)
sum_axis0 = np.sum(array,axis=0,dtype=float) #Sums all values of columns and prints 1dim horizontal vector
sum_axis1 = np.sum(array,axis=1,dtype=float) #Sums all values of columns and prints 1dim vertical vector
mean_total = np.mean(array) #basically "sum(array,axis,None) / array.size" Output is sum/size
mean_axis0 = np.mean(array,axis=0)
mean_axis1 = np.mean(array,axis=1)
standard =  np.std(array) #OUT: 0.4714045207910317
variance = np.var(array) #OUT: 0.2222222222222222
min = np.min(array2)
min = np.min(array2,axis=0) #axis0 =  columns
min = np.min(array2,axis=1) #axis1 = rows
max = np.max(array2)
max = np.max(array2,axis=0)
max = np.max(array2,axis=1)
transposed_array2 = np.transpose(array2) #or array2.T
sorted =  np.sort(array)