# Напишите программу с классом Math. При
# инициализации атрибутов нет. Реализовать методы addition,
# subtraction, multiplication и division. При передаче в методы
# двух числовых параметров нужно производить с
# параметрами соответствующие действия и печатать ответ.
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        print(self.a * self.b)

    def __add__(self, other):
        print(self.a + self.b)

    def __sub__(self, other):
        print(self.a - self.b)

    def __truediv__(self, other):
        print(self.a / self.b)

c = Math(1, 2)
print(c + c)
print(c * c)
print(c - c)
print(c / c)