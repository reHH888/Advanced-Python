'''
Question 12: Store and Display Car Information to Represent each car as a
dictionary and store all car dictionaries in a list.
Write a Python program that represents each car as a dictionary and stores all
car dictionaries in a list.
• Create a list of dictionaries called cars, where each dictionary represents a
car and contains the following keys:
o "name" (car model)
o "color" (car color)
o "price" (car price)
o "speed" (maximum speed)
• Use a loop to iterate through the cars list and print each car’s details.
'''

# Create a list of dictionaries representing cars
cars = [
    {"name": "Toyota", "color": "Red", "price": 25000, "speed": 180},
    {"name": "BMW", "color": "White", "price": 40000, "speed": 240},
    {"name": "Mercedes", "color": "Silver", "price": 45000, "speed": 260}
]

# Print each car's details
for car in cars:
    print(f"Car Name: {car['name']}")
    print(f"Color: {car['color']}")
    print(f"Price: ${car['price']}")
    print(f"Speed: {car['speed']} km/h")
    print()