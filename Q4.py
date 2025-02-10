'''
Question 4: Print Multiplication Table
Write a Python program that prints the multiplication table of a given number
using a for loop.
Requirements:
• Create a variable num to store the input number.
• Use a for loop with range() to iterate from 1 to 10.
• Print the multiplication table in the format: {num} x {i} = {result}.
'''
# Create a variable num to store the input number.
num = int(input("Enter a number: "))
# Use a for loop with range() to iterate from 1 to 10.
# Print the multiplication table in the format: {num} x {i} = {result}.
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
