import numpy as np

def divided_differences(x, y):
    """
    Compute the divided difference table for the given data points.
    
    Parameters:
    x : list or np.array
        The x-coordinates of the data points.
    y : list or np.array
        The y-coordinates of the data points.
    
    Returns:
    np.array
        The divided difference coefficients.
    """
    n = len(x)
    dd = np.zeros((n, n))
    dd[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            dd[i, j] = (dd[i + 1, j - 1] - dd[i, j - 1]) / (x[i + j] - x[i])
    
    return dd[0]

def newton_polynomial(x, coefficients, x_eval):
    """
    Evaluate the Newton polynomial at a given point.
    
    Parameters:
    x : list or np.array
        The x-coordinates of the data points.
    coefficients : list or np.array
        The divided difference coefficients.
    x_eval : float
        The point at which to evaluate the polynomial.
    
    Returns:
    float
        The value of the polynomial at x_eval.
    """
    n = len(coefficients)
    result = coefficients[0]
    product = 1
    
    for i in range(1, n):
        product *= (x_eval - x[i - 1])
        result += coefficients[i] * product
    
    return result

def main():
    # Data points
    x = np.array([1, 2, 3, 4])
    y = np.array([1, 4, 9, 16])
    
    # Compute divided differences
    coefficients = divided_differences(x, y)
    
    # Points to evaluate
    x_eval = np.linspace(1, 4, 100)
    y_eval = [newton_polynomial(x, coefficients, xi) for xi in x_eval]
    
    # Plotting
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'ro', label='Data points')
    plt.plot(x_eval, y_eval, 'b-', label='Newton interpolation polynomial')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Newton Polynomial Interpolation')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
