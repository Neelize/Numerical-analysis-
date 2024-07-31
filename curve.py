import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the model function (e.g., a quadratic function)
def model_function(x, a, b, c):
    return a * x**2 + b * x + c

# Generate synthetic data with noise
np.random.seed(0)  # For reproducibility
x_data = np.linspace(-10, 10, 100)
y_data = model_function(x_data, 1, 2, 3) + np.random.normal(0, 5, x_data.size)

# Perform curve fitting
initial_guess = [1, 1, 1]  # Initial guess for the parameters
popt, pcov = curve_fit(model_function, x_data, y_data, p0=initial_guess)

# Extract the fitted parameters
a_fit, b_fit, c_fit = popt

# Generate the fitted curve
y_fit = model_function(x_data, *popt)

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Data', color='red')
plt.plot(x_data, y_fit, label='Fitted curve', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Curve Fitting Example')
plt.show()

# Print the fitted parameters
print(f"Fitted parameters: a = {a_fit}, b = {b_fit}, c = {c_fit}")
