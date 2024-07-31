import sympy as sp

def differentiate_single_variable():
    # Define the variable and the function
    x = sp.symbols('x')
    f = x**3 + 2*x**2 + 3*x + 4
    
    # Compute the first derivative
    f_prime = sp.diff(f, x)
    print(f"First derivative of f(x): {f_prime}")
    
    # Compute the second derivative
    f_double_prime = sp.diff(f, x, 2)
    print(f"Second derivative of f(x): {f_double_prime}")

def differentiate_multivariable():
    # Define the variables
    x, y = sp.symbols('x y')
    g = x**2 * y + y**3
    
    # Compute partial derivatives
    g_diff_x = sp.diff(g, x)  # Partial derivative with respect to x
    g_diff_y = sp.diff(g, y)  # Partial derivative with respect to y
    
    print(f"Partial derivative of g(x, y) with respect to x: {g_diff_x}")
    print(f"Partial derivative of g(x, y) with respect to y: {g_diff_y}")

if __name__ == "__main__":
    print("Differentiation of single variable function:")
    differentiate_single_variable()
    
    print("\nDifferentiation of multivariable function:")
    differentiate_multivariable()
