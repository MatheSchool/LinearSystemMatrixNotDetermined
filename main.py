import numpy as np
from time import time

n = np.matrix([[2, 2, 3], [-1, 1, 1], [1, 3, 4]]);
m = np.matrix([[1], [0], [-4]]);

print("n =")
print(n);
print("m =")
print(m)

start_time = time()
x = np.linalg.inv(n) * m;
end_time = time()
eleapse_time = end_time - start_time

print("x =")
print (x);

print("Elapsed time: %0.10f seconds." % eleapse_time)
print()