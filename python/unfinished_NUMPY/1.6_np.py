import numpy as np
#transpose
array = np.array([(1,2,3),(4,5,6),(7,8,9)])
# 147,258,369 olmali
print(array.transpose())
#or
transposed_array = np.transpose(array)
print(transposed_array)
#or
transposed_array2 = array.T
print(transposed_array2)

#reshaping
array2 = np.random.randint(1,10,(3,2))
print(array2)
#output:
#[[8 7]
# [2 8]
# [3 5]

reshaped_array2 = array2.reshape(2,3)
print(reshaped_array2)
#output:
#[[8 7 2]
# [8 3 5]]