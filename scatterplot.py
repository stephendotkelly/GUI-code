import matplotlib.pyplot as plt
x = [100,200,300,400,500,600,700,800]
y = [500,200,400,200,100,400,500,200]

plt.scatter(x,y, label='Tag/Anchor Location', color='k')
plt.xlabel('x')
plt.ylabel('y')
plt.title('GPS Points')
plt.legend()
plt.show()