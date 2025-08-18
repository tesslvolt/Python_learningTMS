import math

# я так понял тут нужно посчитать погрешность между программным и "ручным"
# вычислением синуса, поэтому сделаю так

x = int(input("Введите x: "))

manually = 0
for n in range(10):
    manually += ((-1) ** n) * (x ** (2 * n + 1) / math.factorial(2 * n + 1))

program = math.sin(x)

difference = int(abs(manually - program))

print(f"Вычисление синуса программно: {program},вычисление синуса вручную: {manually} и их разница равна = {difference} ")

