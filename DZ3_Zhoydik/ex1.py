'''
Есть три целочисленные переменные, нужно посчитать:
● сумму
● разность
● произведение
● от первой переменной отнять вторую и прибавить третью
● поделить произведение двух переменных на третью
● от суммы первых двух переменных найти остаток от деления
на третью переменную
'''

value_1 = int(input("Введите переменную 1:"))
value_2 = int(input("Введите переменную 2:"))
value_3 = int(input("Введите переменную 3:"))

result = value_1 + value_2 + value_3
print(result)

result = value_1 - value_2 - value_3
print(result)

result = value_1 * value_2 * value_3
print(result)

result = value_1 * value_2 / value_3
print(result)

result = (value_1 + value_2) % value_3
print(result)
