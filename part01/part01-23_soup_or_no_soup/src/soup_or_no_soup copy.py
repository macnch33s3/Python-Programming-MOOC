# Write your solution here
name = input("Please tell me your name: ")

if name != 'Jerry':
    portions = int(input("How many portions of soup? "))
    tcost = float(portions * 5.90)
    print(f"The total cost is {tcost}")
    print("Next please!")

else:
    print("Next please!")
