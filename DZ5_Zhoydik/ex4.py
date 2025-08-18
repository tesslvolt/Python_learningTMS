numbers = [1, 2, 3, 4, 5]
i = 0
sum = 0

while i < len(numbers):
    sum += numbers[i]
    i += 1

print("Cумма чисел в списке: ", sum)
print("Наименьшее число в списке:", min(numbers))
print("Наибольшее число в списке:", max(numbers))