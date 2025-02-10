'''
Question 6: Countdown Using a While Loop
Write a Python program that takes a number and counts down to 0 using a while
loop.
Requirements:
• Create a variable num to store the input number.
• Use a while loop to decrease the value of num until it reaches 0.
• Print each number during the countdown.
Example Output (for num = 5):
5
4
3
2
1
0
Countdown complete!
'''
# Create a variable num to store the input number.
num = 13
# Use a while loop to decrease the value of num until it reaches 0.
# Print each number during the countdown.
while num >= 0:
    print(num)
    num -= 1
print("Countdown complete!")
