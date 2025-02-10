'''
Question 3: Write a Python program that classifies an employee's performance
based on their performance rating.
Requirements:
• Create a variable named employee to store the employee's name.
• Create a variable named rate to store the employee's performance rating (a
number between 1 and 5, where 5 is the highest).
• Implement the following rating system:
o If the rate is 5 or higher, print "Your Rate Is Excellent".
o If the rate is between 3 and 4 (inclusive), print "Your Rate Is Good".
o If the rate is between 2 and 2.99, print "Your Rate Is Bad".
o If the rate is below 2, print "Your Rate Is Very Bad".
'''

employee = "Adam"
rate = 3.55

# If the rate is 5 or higher, print "Your Rate Is Excellent".
if rate >= 5:
  print(f"Your Rate Is Excellent for {employee}")

# If the rate is between 3 and 4 (inclusive), print "Your Rate Is Good".
elif rate >= 3 and rate <= 4:
  print(f"Your Rate Is Good for {employee}")

# If the rate is between 2 and 2.99, print "Your Rate Is Bad".
elif rate >= 2 and rate < 3:
  print(f"Your Rate Is Bad for {employee}")

# If the rate is below 2, print "Your Rate Is Very Bad".
else:
  print(f"Your Rate Is Very Bad for {employee}")
