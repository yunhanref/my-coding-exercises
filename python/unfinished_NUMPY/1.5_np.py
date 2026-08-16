import numpy as np
#normal python lists dont have math operations as default, they can only be addded end to end.
pylist1 = [1,2,3]
pylist2 = [10,11,12]
print(pylist1 + pylist2) #output will be: [1, 2, 3, 10, 11, 12]. No math happened
nplist1 = np.random.randint(1,10,(3,3))
nplist2 = np.random.randint(1,10,(3,3))
print(f"list1:  ({nplist1}) + list2:  ({nplist2}) = {nplist1 + nplist2}")
