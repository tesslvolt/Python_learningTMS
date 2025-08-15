'''
Дано трехзначное число, найти сумму его цифр.
 Например,дано 123 – сумма 6, дано 555, сумма 15.
'''

number = int(input("Введите трехзначное число: "))
length_number = len(str(number))

while length_number != 3:
    number = int(input("Введите ТРЕХЗНАЧНОЕ число:"))
    length_number = len(str(number))
    if length_number == 3:
        break

first_number = number // 100
middle_number = number % 100 // 10
lust_number = number % 10

print(first_number + middle_number + lust_number)