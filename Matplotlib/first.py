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
    :Create empty figure and add a set of axes to 
    it. > fig = plt.figure()
"""

fig = plt.figure()
# axes1 = fig.add_axes([left, bottom, width, height])
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes
# 20% from the left, 50% from bottom, 40% of width, 30% of total height

# Larger Figure Axes 1
axes1.plot(x, y, 'b')
axes1.set_xlabel('X_label_axes2')
axes1.set_ylabel('Y_label_axes2')
axes1.set_title('Axes 2 Title')
plt.show()

# Insert Figure Axes 2
axes2.plot(y, x, 'r')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title')
# plt.show()

"""
Using subplots is more efficient compared
to using plt.figure()
"""
fig, axes = plt.subplots(nrows=1, ncols=2)
for ax in axes:
    ax.plot(x, y, 'g')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

# fig    
# plt.tight_layout()

"""Figure size and DPI"""
fig, axes = plt.subplots(figsize=(12,3))
