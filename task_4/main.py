import math 
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
h = ((10 * ((pow(x, 1/3)) ** 1/2) + pow(x, y + 2))) * ((math.asin(z)) ** 2 - abs(x-y))
print(f"Результат = {h = }") 