number = input("Please type in a number: ")
if number > 100:
    print("The number was greater than one hundred")
    number - 100
    print("Now its value has decreased by one hundred)
     print("Its value is now"+ number)
print(number + " must be my lucky number!")
print("Have a nice day!)



#--------------------------------------------------------------------------
#hwage = float(input("Hourly wage: "))
#hours = int(input("Hours worked: "))
#day = input("Day of the week: ")

hwage   = 20.0
hours   = 6
day     = "Sunday"

dwages = hwage * hours
print("condition:", day == "Sunday")
if day == "Sunday":
    print("wages before:", dwages)
    dwages *= 2
    print("wages after:", dwages)

print(f"Daily wages: {dwages} euros")