import numpy as np
import sympy as sp

def lagrange_interpolation_coefficients(x_points, y_points):
    # Define the symbol for polynomial variable
    x = sp.symbols('x')
    
    # Number of data points
    n = len(x_points)
    
    # Initialize the Lagrange polynomial
    L = 0
    
    # Compute the Lagrange basis polynomials
    for i in range(n):
        xi = x_points[i]
        yi = y_points[i]
        
        # Compute L_i(x)
        Li = 1
        for j in range(n):
            if i != j:
                xj = x_points[j]
                Li *= (x - xj) / (xi - xj)
        
        # Add the weighted L_i(x) to the polynomial
        L += yi * Li
    
    # Convert the polynomial to standard form and get coefficients
    L_poly = sp.expand(L)
    coefficients = sp.Poly(L_poly, x).all_coeffs()
    
    # Convert coefficients from symbolic to numeric
    coefficients = [float(c) for c in coefficients]
    
    return coefficients

# Given data points
x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]

# Compute the coefficients
coefficients = lagrange_interpolation_coefficients(x_points, y_points)

print("Coefficients of the Lagrange interpolating polynomial:")
print(coefficients)
