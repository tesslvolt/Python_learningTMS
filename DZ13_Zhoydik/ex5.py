# Создайте класс Calculator, который использует разные
# стратегии для выполнения математических операций.
# ● Создайте несколько классов, каждый реализует
# определенную стратегию математической операции,
# например, Addition, Subtraction, Multiplication, Division.
# Каждый класс должен содержать метод execute, который
# принимает два числа и выполняет соответствующую
# операцию.
# ● Calculator должен иметь метод set_strategy, который
# устанавливает текущую стратегию, и метод calculate,
# который выполняет операцию с помощью текущей стратегии.
import numbers
from abc import ABC, abstractmethod

class TwoNumbers(ABC):
    @abstractmethod
    def execute(self, x, y):
        pass

class Addition(TwoNumbers):
    def execute(self, x, y):
     print(f"ответ сложение: {x + y}")


class Subtraction(TwoNumbers):
    def execute(self, x, y):
        print(f"ответ вычитание: {x - y}")


class Multiplication(TwoNumbers):
    def execute(self, x, y):
        print(f"ответ умножение : {x * y}")

class Division(TwoNumbers):
    def execute(self, x, y):
        try:
            print(f"ответ деление: {x / y}")
        except ZeroDivisionError:
            raise ZeroDivisionError("На ноль делить нельзя")




class Calculator:
    def set_strategy(self, numbers):
        self.numbers = numbers

    def calculate(self, x, y):
        self.numbers.execute(x, y)


calc = Calculator()
calc.set_strategy(Addition())
calc.calculate(2, 3)
calc.set_strategy(Subtraction())
calc.calculate(3, 3)
calc.set_strategy(Multiplication())
calc.calculate(6, 3)
calc.set_strategy(Division())
calc.calculate(4, 2)





