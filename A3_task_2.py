'''
Task 2: Using the Math Module for Calculations

Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

'''
import math

n=int(input("Enter a number: "))
sq_root=math.sqrt(n)
log=math.log(n)
sine=math.sin(n)

print(f"The square root of {n} is {sq_root}")
print(f"The natural logarithm of {n} is {log}")
print(f"The natural logarithm of {n} is {sine}")