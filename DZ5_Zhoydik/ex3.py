times = int(input("Введите количество чисел в последовательности Фибоначчи: "))

i = 0

numbers = [1, 2]

print(numbers[1])
print(numbers[2])

while i < times:

    next_number = numbers[-1] + numbers[-2]
    numbers.append(next_number)
    i += 1

print(numbers)