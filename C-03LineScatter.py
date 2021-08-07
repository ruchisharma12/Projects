import matplotlib.pyplot as plt 
import numpy as np

x = (1,2,3,4,5)
y = (3,4,5,6,7)
z = (5,10,15,20,25)

plt.plot(x,z,color='blue')
plt.plot(y,z,'+')
plt.plot(x,y,'*')

plt.xlabel('x-values')
plt.ylabel('y-values')
plt.title('line plot')
plt.grid(True)
plt.show()