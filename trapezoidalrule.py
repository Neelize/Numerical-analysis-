import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return np.sin(x)  # Define the function to integrate

def trapezoidal_rule(a, b, n):
    # Generate n+1 evenly spaced points between a and b
    x = np.linspace(a, b, n+1)
    y = f(x)
    
    # Compute the width of each trapezoid
    h = (b - a) / n
    
    # Compute the integral using the trapezoidal rule
    integral = (h / 2) * np.sum(y[:-1] + y[1:])
    return integral

def main():
    # Define the integration interval
    a = 0  # Lower limit
    b = np.pi  # Upper limit
    n = 100  # Number of trapezoids
    
    # Compute the integral using the trapezoidal rule
    integral_trap = trapezoidal_rule(a, b, n)
    
    # Compute the exact integral using SciPy's quad function
    integral_exact, error = quad(f, a, b)
    
    # Print the results
    print(f"Trapezoidal rule estimate: {integral_trap:.6f}")
    print(f"Exact integral: {integral_exact:.6f}")
    print(f"Error estimate: {error:.6e}")
    
    # Plot the function and trapezoids
    x = np.linspace(a, b, 500)
    y = f(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', label='f(x)')
    plt.fill_between(x, y, alpha=0.2, label='Area under curve')
    
    # Plot trapezoids
    x_trap = np.linspace(a, b, n+1)
    y_trap = f(x_trap)
    plt.step(x_trap, y_trap, 'r--', where='post', label='Trapezoidal approximation')
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Trapezoidal Rule Approximation')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
