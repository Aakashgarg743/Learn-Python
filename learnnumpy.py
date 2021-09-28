import numpy as np
arr = np.array([1,2,3])
print(arr)
arr2 = np.array([(1,2,3),(4,5,6)])
print(arr2)

# CHECKING - OCCUPIES LESS MEMORY
import sys
l1 = range(10000)
print(sys.getsizeof(5) * len(l1))

a1 = np.arange(10000)
print(a1.size*a1.itemsize)

# CHECKING - TIME
import time
size = 10000000
l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
re = [(x,y) for x, y in zip(l1,l2)]
print(re)
print((time.time()-start)*1000)

start = time.time()
result = a1+a2
print((time.time()-start)*1000)

# NUMPY OPERATIONS
a = np.array([(1,2,3), (4,5,6)])
b = np.array([(1,2,3), (4,5,6)])
print(a)
print(a.ndim)
print(a.itemsize)
print(a.dtype)
print(a.size)
print(a.shape)
print(a.reshape(3,2))
print(a)
print(a[1, 2])
print(a[0:,2])
a = np.linspace(0,14,100)
print(a)
print(a.min())
print(a.max())
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))
print(np.sqrt(a))
print(np.std(a))
print(np.vstack((a,b)))
print(np.hstack((a,b)))
print(a.ravel())
print(np.exp(a))
print(np.log(a))
print(np.log10(a))

import matplotlib.pyplot as plt
a = np.arange(0, 3*np.pi, 0.1)
print(np.pi)
print(a)
x = np.sin(a)
y = np.cos(a)
plt.plot(x)
plt.plot(y)
plt.show()