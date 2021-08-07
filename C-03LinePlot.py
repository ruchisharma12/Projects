import matplotlib.pyplot as plt 
import numpy as np

x = (1,2,3,3,3,3)
y = (0,1,2,4,8,10)


plt.plot(x,y,color='blue')


plt.xlabel('x-values')
plt.ylabel('y-values')
plt.title('line plot')
plt.grid(True)
plt.show()