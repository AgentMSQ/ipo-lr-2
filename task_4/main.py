import math #библиотека
x = float(input("x = ")) #вводим х
y = float(input("y = ")) #вводим y
z = float(input("z = ")) #вводим z
h = ((10 * ((pow(x, 1/3)) ** 1/2) + pow(x, y + 2))) * ((math.asin(z)) ** 2 - abs(x-y)) #вычисляем выражение 
print(f"Результат = {h = }") #выводим