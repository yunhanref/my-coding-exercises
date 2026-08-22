import numpy as np
#create an array of zeros
zeros = np.zeros((2,2))
print(zeros)
#create an array if ones
ones = np.ones((3,3))
print(ones)
#create an array of a particular value
full  = np.full((4,4),1)
print(full)
#create an identity matrix (birim matris, birler kosegeni matris)
#create manually:
manual_identity = np.array([(1,0,0),(0,1,0),(0,0,1)])
print(manual_identity)
numpy_identity = np.eye(2) #2x2 kare matris
print(numpy_identity)
#or
numpy_identity2 = np.identity(3) #3x3 kare matris
print(numpy_identity2)
#create a array with random numbers
random = np.random.random((5,5)) #values are between zero and one
random2 = np.random.randint(10,100,(5,5)) #(range,range,(matrix shape))
print(random)
print(random2)
#create an array with evenly spaced values
linspace = np.linspace(10,30,5) #(start,end,jumpingvalue)
print(linspace)
#convert list to np array
listtoconvert = [1,2,3,4,5]
convertedlist = np.asarray(listtoconvert)
print(f"list: {convertedlist}, type: {type(convertedlist)}") #[1 2 3 4 5]
#convert a tuple to np array
tupletoconvert = (1,2,3,4,5)
convertedtuple = np.asarray(tupletoconvert)
print(f"tuple:  {convertedtuple}, type: {type(convertedtuple)}")