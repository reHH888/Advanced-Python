'''
Question 5: Sum of Even Numbers
Write a Python program that calculates the sum of even numbers from 1 to n
using a for loop.
Requirements:
• Create a variable n to store the input number.
• Use a for loop with range() to iterate from 1 to n.
• Add only even numbers to the sum.
• Print the total sum at the end.
'''
# Create a variable n to store the input number.
n = 24
sum = 0
# Use a for loop with range() to iterate from 1 to n.
# Add only even numbers to the sum.
# Print the total sum at the end.
for i in range(1, n+1):
    if i % 2 == 0:
        sum += i
print(f"The sum of even numbers from 1 to {n} is {sum}.")

