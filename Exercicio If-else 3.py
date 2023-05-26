# Exercise 3: Leap Year
# Write a program that takes a year as input from the user and determines if it is a leap year or not.
# A leap year is divisible by 4, except for years that are divisible by 100 but not divisible by 400.

Year = int(input("Write a year: "))

if Year % 4 == 0 and (Year % 100 != 0 or Year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")
