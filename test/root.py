import math as m

# Define the function for which you want to find the root.
def g(x):
    # Define your fixed-point iteration formula here.
    return (m.e**x+2)/3

# Initial guess for the root.
x0 = 1.0

# Tolerance level for convergence.
tolerance = 1e-6

# Maximum number of iterations.
max_iterations = 100

# Fixed-point iteration loop.
for i in range(max_iterations):
    x1 = g(x0)  # Apply the fixed-point formula.
    
    # Check for convergence.
    if abs(x1 - x0) < tolerance:
        print(f"Converged to root: {x1} after {i+1} iterations.")
        break
    
    x0 = x1  # Update the previous estimate with the new one.
else:
    print("Fixed-point iteration did not converge within the specified number of iterations.")

