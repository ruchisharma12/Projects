import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9]
y=[5,2,4,2,1,4,5,2,6]


plt.scatter(x,y, label='skitscat', color='k')

plt.title('Scatter')
plt.xlabel('X')
plt.ylabel('Y')

plt.legend()

plt.show()
