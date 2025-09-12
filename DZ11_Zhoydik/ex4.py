# Программа с классом Sphere для представления сферы
# в трёхмерном пространстве. Реализовать методы:
# ● конструктор, принимающий 4 числа: радиус и координаты
# центра сферы x, y, z. Если конструктор вызывается без
# аргументов, создать объект сферы с единичным радиусом
# и центром в начале координат. Если конструктор
# вызывается только с радиусом, создать объект с
# соответствующим радиусом и центром в начале
# координат
# ● метод get_volume(), возвращающий число – объем шара,
# ограниченного текущей сферой
# Продолжение ->
# ● метод get_square(), возвращающий число – площадь
# внешней поверхности сферы
# ● метод get_radius(), возвращающий число – радиус текущей
# сферы
# ● метод get_center(), возвращающий кортеж с координатами
# центра сферы
# ● метод set_radius(radius), который принимает новое
# значение радиуса, меняет радиус текущей сферы и ничего
# не возвращает
# ● метод set_center(x, y, z), который принимает новые
# значения для координат центра радиуса, меняет
# координаты текущей сферы и ничего не возвращает
# ● метод is_point_inside(x, y, z), который принимает
# координаты некой точки в трёхмерном пространстве и
# возвращает True или False в зависимости от того,
# находится ли точка внутри сферы
class Sphere:

    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def location(self):
        print(f"radius: {self.radius} [x: {self.x}, y: {self.y}, z: {self.z}]")

    def get_volume(self):
        volume = (4/3) * 3.14 * self.radius ** 3
        print(f"Объем шара: {volume}")

    def square(self):
        print(f"площадь сферы: {4 * 3,14 * self.radius ** 2}")

    def radius(self):
        print(f"радиус: {self.radius}")

    def get_center(self):
        print((self.x, self.y, self.z))

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self):
        x1 = int(input("x: "))
        y1 = int(input("y: "))
        z1 = int(input("z: "))
        dis = ((x1 - self.x) ** 2 + (y1 - self.y) ** 2 + (z1 - self.z) ** 2) ** 0.5
        if dis < self.radius:
            print("точка внутри сферы")
        else:
            print("точка за пределами сферы")

s = Sphere(2)
s.location()
s.get_volume()
s.get_center()
s.is_point_inside()