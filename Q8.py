'''
Question 8: Sum of List Elements
Write a Python program that calculates the sum of all numbers in a list.
Example:
numbers = [10, 20, 30, 40, 50]
Expected Output:
Sum of numbers: 150
'''
# Create a list of numbers.
numbers = [30, 20, 80, 60, 50]

# Initialize a variable to store the sum.
total = 0

# Iterate over each number in the list and add it to the sum.
for number in numbers:
    total += number

# Print the final sum after the loop ends.
print(f"Sum of numbers: {total}")


