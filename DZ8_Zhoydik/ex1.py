# Реализовать программу для подсчёта индекса массы
# тела человека. Пользователь вводит рост и вес с клавиатуры.
# На выходе – ИМТ и пояснение к нему в зависимости от
# попадания в тот или иной диапазон. Использовать обработку
# исключений.

def index_mas(weight, height):
    if height <= 0:
        raise ValueError("Рост не может быть равен нулю или отрицательным.")
    if weight <= 0:
        raise ValueError("Вес не может быть равен нулю или отрицательным.")

    imt = weight / (height ** 2)
    return imt


def imt_cat(imt):
    if imt < 18.5:
        return "Кому-то нужно больше кушать"
    elif 18.5 <= imt < 24.9:
        return "Норма"
    elif 25 <= imt < 29.9:
        return "Кому-то нужно меньше кушать"
    else:
        return "Ожирение"

try:
    weight = float(input("Введите ваш вес в кг: "))
    height = float(input("Введите ваш рост в метрах: "))

    imt = index_mas(weight, height)
    print(f"Ваш индекс массы тела: {imt:.2f}")
    print(imt_cat(imt))

except ValueError as e:
    print(f"Ошибка ввода: {e}")