import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

print("x is", x)
print("y is", y)

"""
Functional Method

plt.plot(*args, **kwargs)
in our case: plt.plot(x,y)
"""
plt.plot(x,y)
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
# plt.show() # Prints out the plot

"""MUltiple plots on the same canvas"""
plt.subplot(1,2,1)
plt.plot(x, y, 'r--') # More on color options later
plt.subplot(1,2,2)
plt.plot(y, x, 'g*-');
# plt.show()

"""
Object Oriented Method
"""
