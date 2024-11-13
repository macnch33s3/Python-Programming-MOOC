# Write your solution here
number = int(input("Please type in a number: "))
if number < 0:
    abs = number * -1
    print(f"The absolute value of this number is {abs}")
else:
    print(f"The absolute value of this number is {number}")