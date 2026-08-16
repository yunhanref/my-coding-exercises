import numpy as np
#creating an array we like
a = np.array([1, 2, 3, 4, 5, 6]) #created an array list of numbers
for i in a:
  print(i) #travels each index and prints it individually each turn.
print(a) #prints the whole array
print(a[1]) #reaches the index 1 and prints its value which is `2`
a.shape #prints the shape of the array (columns,rows) output will be (6,) because this is a 1D array
b = np.array([(1,2,3),(4,5,6)])
print(b) #2D array