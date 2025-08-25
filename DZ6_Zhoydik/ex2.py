#  Программа получает на вход число в десятичной
# системе счисления. Реализовать функцию, которая
# переводит входное число в двоичную систему счисления.
# Допускается реализация функции как в рекурсивном
# варианте, так и с итеративным подходом.
number_decimal = float(input("Введите число в десятичной системе исчисления: "))

def InterpritationWholePart(number):

    number_for_while = int(number)
    binary_wh = []

    while number_for_while > 0:
        remainder = number_for_while % 2
        number_for_while //= 2
        binary_wh.append(remainder)

    binary_wh.reverse()
    whole = "".join(str(item) for item in binary_wh)
    print(whole)

    if isinstance(number, float):

        binary_fr = []
        i = 0
        int_number = number // 1
        fractional = number - int_number

        while i < 4:
            fractional *= 2 # 0.28
            bit = int(fractional)
            binary_fr.append(bit)
            fractional -= bit
            i +=1

        fraction = "".join(str(item) for item in binary_fr) #   перебором записываем числа в строку
        print(f"Число {number} в двоичном коде будет таким: {whole},{fraction}")

    elif isinstance(number, int):
        print(f"Число {number_decimal} в двоичном коде будет таким: {whole}")

InterpritationWholePart(number_decimal)


