import numpy as np 
import matplotlib.pyplot as plt

n = np.arange(0,10)
x_n = np.sin(0.2* np.pi*n)
plt.stem(n,x_n)
plt.title('Discrete Tome Signal')
plt.xlabel ('n')
plt.ylabel ('x[n]')
plt.show() # prosoxh parenthesh sth show

# USE ARANGE


#--------------------------------#Continuous----------------------------

#USE LINSPACE + [PLOT]
import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(0 , 4* np.pi , 1000)

y = np.sin(x)
plt.plot(x,y)
plt.title('Continuous Time Signal of sinx from 0 to 4')
plt.xlabel ('x')
plt.ylabel ('sin[n]')
plt.grid(True)
plt.show()

# gia 2 h perissoteres grafikes . an den xrhsimopoiw thn figure , mpainoun ola se ena parathuto . 

#d[n]


import numpy as np
import matplotlib.pyplot as plt


n = np.arange (-10 , 11)

delta = np.where(n== 0 , 1 , 0 )
#delta = (n==0).astype(int)

u = np.where(n>= 0 , 1 , 0 )
#u = (n>=0).astype(int)

r = np.where(n>= 0 , n , 0 )
#r = n*(n>=0).astype(int)


e_n = u = np.where(n>= 0 , np.exp(n) , 0 )
#e_n = np.exp(n) *(n>=0).astype(int)

plt.subplot(2,2,1)
plt.stem(n,delta)
plt.title ('UnitImpulse Signal ')
plt.xlabel('n')
plt.ylabel('delta[n]')
plt.grid(True)
plt.show()





