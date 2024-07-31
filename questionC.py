import numpy as np

# Define the data points
x_points = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y_points = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# Define the x value where we want to interpolate
x_to_interpolate = 4.0

# Find the interval that contains the x value
for i in range(len(x_points) - 1):
    if x_points[i] <= x_to_interpolate <= x_points[i + 1]:
        x1, x2 = x_points[i], x_points[i + 1]
        y1, y2 = y_points[i], y_points[i + 1]
        break

# Apply the linear interpolation formula
y_interpolated = y1 + (x_to_interpolate - x1) * (y2 - y1) / (x2 - x1)

print(f"The interpolated value of y at x = {x_to_interpolate} is {y_interpolated:.2f}")
