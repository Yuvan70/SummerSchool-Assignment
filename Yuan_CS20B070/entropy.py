#assignment 1 1st question cs20b070

import numpy as np

n = 100

y = np.random.randint(0,2,(1,n))
y_cap = np.random.rand(n)

entropy = (-1/n)*((np.sum(y*np.log2(y_cap))) + (np.sum((1-y)*(np.log2(1-y_cap)))))

print("The cross entropy is")
print(entropy)