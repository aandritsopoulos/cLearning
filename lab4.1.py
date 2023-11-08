import numpy as np 
import matplotlib.pyplot as plt

n = np.arange(0,10)
x_n = np.sin(0.2* np.pi*n)
plt.stem(n,x_n)
plt.title('Discrete Tome Signal')
plt.xlabel ('n')
plt.ylabel ('x[n]')
plt.show() # prosoxh parenthesh sth show


