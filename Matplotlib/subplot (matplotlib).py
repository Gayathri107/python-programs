import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2*np.pi*x1)*np.exp(-x1)
y2 = np.cos(2*np.pi*x2)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('Subplot 1')
plt.xlabel('x1')
plt.ylabel('y1')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '--')
plt.title('Subplot 2')
plt.xlabel('x2')
plt.ylabel('y2')

plt.show()
