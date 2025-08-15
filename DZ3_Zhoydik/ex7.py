'''
Дано трехзначное число, найти количество его десятков.
Например, дано 123 – количество десятков: 2, дано 978 –
количество десятков: 7.
'''

number = int(input("Введите трезначное число: "))

length_number = len(str(number))

while length_number != 3:
    number = int(input("Введите ТРЕХЗНАЧНОЕ число:"))
    length_number = len(str(number))
    if length_number == 3:
        break

print(int((number % 100) // 10))

