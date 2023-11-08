import numpy as np
import matplotlib.pyplot as plt

n = np.arange ( -10 , 10 )
x1 = ( -n-4 >=0 ).astype(int)
x2 = 2* (-3-n) * (-3-n>=0)
x3 = -4* (-n+2==0).astype(int)
x4 = abs(2 * (n-3>=0) - 3* x2 - (n - 2) * (n-2>=0) -x3)

x5 = np.sin(n) /n
x5[n == 0 ] = 1 



