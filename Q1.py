
'''
Question 1: Write a Python program that:
1. Declares two variables: num1 and num2 and assigns them integer values of 5
and 6, respectively.
'''
num1 = 5
num2 = 6

# 2. Calculates the sum of num1 and num2 and stores the result in a variable called result.
result = num1 + num2

'''
3. Prints the calculated sum to the console in three different ways:
o Directly print the value of the result variable.
o Print the sum as a string using string concatenation.
o Print the sum using f-string formatting.
'''
print(result)
print(f"The sum is {result}.")
print("The sum is " + str(result) + ".")

'''
4. Demonstrate the use of f-string formatting by printing a formatted message
that includes a variable named firstName (assumed to be defined elsewhere) and
a variable named score.
'''
firstName = "Hoor"
score = 99.2
print(f"The first name is {firstName} and the score is {score}.")

