# Программа получает на вход число. Реализовать
# функцию, которая определяет, является ли это число простым
# (делится только на единицу и на само себя).
number_for_checking = int(input("Введите число для проверки на простоту: "))

def simple_number(number):

   if number_for_checking < 2:
       print("введите число больше 1")

   for n in range(2, int(number ** 0.5) + 1):
      if number % n  == 0:
          print(f"число {number} не является простым")
      else:
          print(f"число {number} является простым")

simple_number(number_for_checking)







