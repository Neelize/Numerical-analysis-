import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Given data points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])

# Create an interpolation function
interp_func = interp1d(x, y, kind='linear')

# Generate new x values for interpolation
x_new = np.linspace(0, 5, 50)
y_new = interp_func(x_new)

# Plot the original data points
plt.scatter(x, y, label='Data points', color='red')

# Plot the interpolated values
plt.plot(x_new, y_new, label='Linear interpolation', color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Simple Interpolation Example')
plt.show()
