# Exercise 1: Positive or Negative
# Write a program that takes an integer input from the user
# and prints "Positive" if the number is greater than zero, and "Negative" otherwise.

num = int(input("Write a Number: "))

if num > 0:
    print(f"The number {num} is Positive")
elif num < 0:
    print(f"The number {num} is Negative")
else:
    print(f"Its {num}")
