"""import numpy as np
import matplotlib.pyplot as plt

n = np.arange ( -10 , 10 )
x1 = ( -n-4 >=0 ).astype(int)
x2 = 2* (-3-n) * (-3-n>=0)
x3 = -4* (-n+2==0).astype(int)
x4 = abs(2 * (n-3>=0) - 3* x2 - (n - 2) * (n-2>=0) -x3)

x5 = np.sin(n) /n
x5[n == 0 ] = 1 """

import numpy as np
import matplotlib.pyplot as plt

n = np.arange( -10 , 10 )
x1 = np.exp(np.abs(n))
e1 = np.sum(np.abs(x1)**2)
print(f'Energy of x1: {e1}')


 






