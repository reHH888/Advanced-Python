'''
Question 7: Password Guessing Program
Write a Python program that asks the user to enter a password. The program
should keep asking until the correct password is entered.
Requirements:
• Set a variable correct_password = "Python123".
• Use a while loop to repeatedly ask for user input.
• If the input matches correct_password, print "Access Granted!" and exit
the loop.
Example Output:
Enter password: hello123
Incorrect password, try again.
Enter password: Python123
Access Granted!
'''
# Set a variable correct_password = "Python123"
correct_password = "Python123"

# Use a while loop to repeatedly ask for user input.
# If the input matches correct_password, print "Access Granted!" and exit the loop.
while True:
  password = input("Enter password: ")
  if password == correct_password:
    print("Access Granted!")
    break
  else:
    print("Incorrect password, try again.")

