from math import sqrt
#input
a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))
if b**2 < (4*a*c):
    print("Nicht definiert, weil negative Diskriminante")

xpos =int(-b + (b**2 - (4*a*c))**(0.5)) / (2*a)
xneg =int(-b - (b**2 - (4*a*c))**(0.5)) / (2*a)

#output
print(f"The roots are {xpos} and{xneg}")