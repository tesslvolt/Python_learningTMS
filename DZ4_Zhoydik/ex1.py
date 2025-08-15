import math

a = int(input("введите число a: "))
b = int(input("введите число b: "))
x = int(input("введите число x: "))


print("итог выполнения функции = ", math.pow(a, 2) / 3 +(math.pow(a, 2) + 4) / b + math.sqrt(math.pow(a, 2) + 4) / 4 +
     math.sqrt(math.pow(math.pow(a, 2) + 4, 3)) / 4)

print("Итог преобразования: ", math.cos(int(x ** 2) ** 2) + math.sin(int(x * 2 - 1) ** 2), end= "рад.")

print("Итог преобразования :", math.sin(x) + math.cos(x), end= "рад.")

print("Итог: ", 5 * x + 3 * x ** 2 * math.sqrt(1 + math.sin(x) ** 2), end= "рад.")