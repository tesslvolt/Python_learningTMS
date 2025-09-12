# Программа с классом Car. При инициализации объекта
# ему должны задаваться атрибуты color, type и year.
# Реализовать пять методов. Запуск автомобиля – выводит
# строку «Автомобиль заведён». Отключение автомобиля –
# выводит строку «Автомобиль заглушен». Методы для
# присвоения автомобилю года выпуска, типа и цвета.
class Car:

    def __init__(self, color, mark, model, year):
        self.color = color
        self.mark = mark
        self.model = model
        self.year = year

    def start(self):
         print("starting")

    def char(self):
        print(self.color, self.mark, self.model, self.year)

    def stop(self):
        print("stopping")


car = Car("WHITE","TOYOTA","MARK2", "1997")
car.start()
car.char()
car.stop()