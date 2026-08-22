import numpy as np
from time import process_time as pt
#this example will show how much faster numpy is than normal python math operations
python_list = [i for i in range(1000000)]
start_time = pt()
for i in python_list:
  i += 5
end_time = pt()
result = end_time-start_time
print(result) #result is 0.05 seconds

#now with numpy speed:
a = np.array([i for i in range(1000000)])
start_time = pt()
a += 5
end_time = pt()
result = end_time-start_time
print(result) #output is 0.0005 seconds
#thats why we use numpy over normal math operations