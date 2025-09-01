# Реализовать программу с функционалом калькулятора
# для операций над двумя числами. Числа и операция вводятся
# пользователем с клавиатуры. Использовать обработку
# исключений.

def calculate(first_number, second_number):
    if operation == "+":
        print(f"Ответ: {first_number + second_number}")
    elif operation == "-":
        print(f"Ответ: {first_number - second_number}")
    elif operation == "*":
        print(f"Ответ: {first_number * second_number}")
    elif operation == "/":
       try:
           division = first_number / second_number
           print(f"Ответ: {division}")
       except ZeroDivisionError as e:
           print(f"Ошибка: {e}")
    else:
        print("такой операции нету")

try:
    first_number = float(input("Введите первое число: "))
    second_number = float(input("Введите второе число: "))
    operation = input("Введите операцию([+], [-], [*], [/]): ")
    calculate(first_number, second_number)
except ValueError as e:
    print(f"Ошибка ввода: {e}")


