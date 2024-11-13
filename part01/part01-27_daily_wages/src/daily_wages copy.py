wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
dotw = str(input("Day of the week: "))

dailywage = (wage * hours)

if dotw == "Sunday":
    sundaywage = dailywage + dailywage
    print(f"Daily wages: {sundaywage} euros")

else:
    print(f"Daily wages: {dailywage} euros")