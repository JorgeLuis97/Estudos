# Exercise 5: Largest of Three Numbers
# Write a program that takes three numbers as input from the user and prints the largest among them.

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is greater than {num2} and {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater than {num1} and {num3}")
elif num3 > num1 and num3 > num2:
    print(f"{num3} is greater than {num2} and {num1}")
