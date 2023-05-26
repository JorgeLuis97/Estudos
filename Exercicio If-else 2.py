# Exercise 2: Maximum of Two Numbers
# Write a program that takes two numbers as input from the user and prints the maximum of the two numbers.

num1 = int(input("Write a Number: "))
num2 = int(input("Write another Number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Equals")
