# Exercise 7: Quadratic Equation Solver
# Write a program that takes the coefficients of a quadratic equation (a, b, c) as input from the user
# and prints the solutions if they exist.
# Handle cases where the equation has real and distinct roots, real and equal roots, or complex roots.
import math

a = int(input("Coefficient A: "))
b = int(input("Coefficient B: "))
c = int(input("Coefficient C: "))

discriminant = b ** 2 - 4 * a * c

print(discriminant)

if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)  # Positive root
    root2 = (-b - math.sqrt(discriminant)) / (2*a)  # Negative root
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    root1 = complex(real_part, imaginary_part)  # Complex root
    root2 = complex(real_part, -imaginary_part)  # Complex root

print(f"Root 1:{root1:.4f}")
print(f"Root 2:{root2:.4f}")
