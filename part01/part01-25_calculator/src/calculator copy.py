num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
oper = str(input("Operation: "))

if oper == "add":
    res = num1 + num2
    print(f"{num1} + {num2} = {res}")

if oper == "multiply":
    res = num1 * num2
    print(f"{num1} * {num2} = {res}")

if oper == "subtract":
    res = num1 - num2
    print(f"{num1} - {num2} = {res}")