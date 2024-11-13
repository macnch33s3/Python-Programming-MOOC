# Write your solution here
name = str(input("What is your name? "))
year = int(input("Which year were you born? "))
currentyear = int(2021)

#Calc
age = currentyear - year

#Output
print(f"Hi {name}, you will be {age} years old at the end of the year {currentyear}")