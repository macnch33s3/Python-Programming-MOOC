#twwo if-statements
number = int(input("Please type in a number: "))

if number < 0:
    print("The number is negative")

if number > 0:
    print("The number is positive or zero")


#if-else
number = int(input("Please type in a number: "))

if number < 0:
    print("The numver is negative")
else:
    print("The number is ppositive or zero")

#another example for string comparison
correct = "herdöpfel"
pw = input("Please type in the password: ")

if pw == correct:
    print("Hello")
else:
    print("No admittance")