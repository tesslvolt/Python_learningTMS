import math

# такая же ситуация

x = int(input("Введите x: "))

manually = 0
for n in range(10):
    manually += ((-1) ** n) * (x ** (2 * n) / math.factorial(2 * n))

program = math.cos(x)

difference = int(abs(manually - program))

print(f"Вычисление синуса программно: {program},вычисление синуса вручную: {manually} и их разница равна = {difference} ")