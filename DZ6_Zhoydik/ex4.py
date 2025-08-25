# Программа получает на вход два числа и находит их
# НОД (наибольший общий делитель). Пример: на вход
# подаются числа 12 и 18, их НОД равен 6.
first_number = int(input("Введите число 1: "))
second_number = int(input("Введите число 2: "))


def nod(number1, number2):
    list_for_first_number = []
    list_for_second_number = []
    similar_number = []

    for n in range(2, int(number1) + 1):
        if number1 % n == 0:
            list_for_first_number.append(n)

    for n in range(2, int(number2) + 1):
        if number2 % n == 0:
            list_for_second_number.append(n)

    for n in list_for_first_number:
        for i in list_for_second_number:
            if n == i:
                similar_number.append(n)

    if similar_number == []:
        print(f"У чисел {first_number} и {second_number} наименьший общий делитель 1 ")
    else:
        print(f"Наибольий общий делитель для чисел {first_number} и {second_number} будет равен {similar_number[-1::]}")

nod(first_number, second_number)












