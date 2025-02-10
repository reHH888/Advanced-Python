'''
Question 10: Access Dictionary Values
Write a Python program that prints the value of a specific key from a dictionary.
Example:
student = {"name": "Mohamed", "age": 16, "grade": "A"}
Expected Output (for key "age"):
The student's age is 16.
'''

student = {"name": "Eli", "age": 20, "grade": "B"}

key = "age"
age = student[key]
print(f"The student's {key} is {age}.")
