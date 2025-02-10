'''
Question 11: Iterate Over a Dictionary
Write a Python program that prints all keys and values in a dictionary using a loop.
Example:
student = {"name": "Ahmed", "age": 15, "grade": "B"}
Expected Output:
name: Ahmed
age: 15
grade: B
'''

student = {"name": "Andria", "age": 19, "grade": "A"}

# Iterate over the dictionary using a loop
for key, value in student.items():
    print(f"{key}: {value}")