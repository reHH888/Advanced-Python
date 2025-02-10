'''
Question 2: Write a Python program that takes two numbers as input from the
user.The program should:
1. Attempt to add the two numbers directly without any type conversion.
2. Then, convert both input values to integers and perform the addition.
3. Finally, convert both input values to floating-point numbers and perform
the addition.
Print the result of each addition operation in a clear and readable format.
'''

# 1. Take two numbers as input from the user.
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# 2. Attempt to add the two numbers directly without any type conversion.
sum = num1 + num2

# 3. Convert both input values to integers and perform the addition.
int_sum = int(num1) + int(num2)

# 4. Convert both input values to floating-point numbers and perform the addition.
float_sum = float(num1) + float(num2)

# 5. Print the result of each addition operation in a clear and readable format.
print("The sum is: ", sum)
print("The Integer sum is: ", int_sum)
print("The Floating-point sum is: ", float_sum)

