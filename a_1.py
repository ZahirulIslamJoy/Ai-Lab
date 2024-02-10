import numpy as np
import matplotlib.pyplot as plt

a = 2
b = 3

x = np.linspace(-10, 10, 50)
fig, ax = plt.subplots(2, 2)

y1 = a * x + b
y2 = a * np.sin(x) + b
y3 = a * x**2 + b
y4= a**x +b 

ax[0, 0].plot(x, y1)
ax[0, 0].set_xlabel('x')
ax[0, 0].set_ylabel('y')
ax[0, 0].set_title('Graph of y = 2x + 3')

ax[0, 0].axhline(0, color='black', linewidth=0.5)
ax[0, 0].axvline(0, color='black', linewidth=0.5)


ax[0, 1].plot(x, y2)
ax[0, 1].set_xlabel('x')
ax[0, 1].set_ylabel('y')
ax[0, 1].set_title('Graph of y =2sinx+3')

ax[0, 1].axhline(0, color='black', linewidth=0.5)
ax[0, 1].axvline(0, color='black', linewidth=0.5)

ax[1, 0].plot(x, y3)
ax[1, 0].set_xlabel('x')
ax[1, 0].set_ylabel('y')
ax[1, 0].set_title('Graph of y =2x^2+3')

ax[1, 0].axhline(0, color='black', linewidth=0.5)
ax[1, 0].axvline(0, color='black', linewidth=0.5)

ax[1, 1].plot(x, y4)
ax[1, 1].set_xlabel('x')
ax[1, 1].set_ylabel('y')
ax[1, 1].set_title('Graph of y =2^x+3')

ax[1, 1].axhline(0, color='black', linewidth=0.5)
ax[1, 1].axvline(0, color='black', linewidth=0.5)

plt.tight_layout()
plt.show()
