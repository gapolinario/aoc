import numpy as np

dy = 9
for i in range(1,dy-1):
    print(i)

print()
for i in range(dy-2,0,-1):
    print(i)

print()
for i in np.concatenate((np.arange(dy//2,0,-1),np.arange(dy//2+1,dy-1))):
    print(i)

print()
for i in np.concatenate((np.arange(dy//2+1,0,-1),np.arange(dy//2+1,dy-1))):
    print(i)