fahr = int(input("Please type in a temperature (F): "))
celsius = (fahr - 32) * 5/9
print(f"{fahr} degrees Fahrenheit equals {celsius} degrees Celsius")

if celsius < 0:
    print("Brr! It's cold in here!")