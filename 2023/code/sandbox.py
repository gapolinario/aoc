import numpy as np

t1 = [1,2,2,3,3,5]
t2 = [3,2,2,3,3,5]

print(np.sum([x1!=x2 for x1,x2 in zip(t1,t2)]))