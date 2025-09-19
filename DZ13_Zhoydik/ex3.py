# Паттерн «Строитель»
# ● Создайте класс Pizza, который содержит следующие
# атрибуты: size, cheese, pepperoni, mushrooms, onions,
# bacon.
# ● Создайте класс PizzaBuilder, который использует паттерн
# «Строитель» для создания экземпляра Pizza. Этот класс
# должен содержать методы для добавления каждого из
# атрибутов Pizza.
# ● Создайте класс PizzaDirector, который принимает
# экземпляр PizzaBuilder и содержит метод make_pizza,
# который использует PizzaBuilder для создания Pizza.
from operator import truediv


class Pizza:
    def __init__(self, size = None, cheese = False, pepperoni = False, mushrooms = False, onions = False, bacon = False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        return  (f"Pizza(Размер:{self.size}, cыр = { self.cheese }, пепперони = {self.pepperoni}"
                 f", грибы = {self.mushrooms}, лук = {self.onions}, бекон = {self.bacon})")


class PizzaBuilder:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def add_size(self, size):
        self.size = size
        return self

    def add_cheese(self, cheese = False):
        self.cheese = cheese
        return self

    def add_pepperoni(self, pepperoni = False):
        self.pepperoni = pepperoni
        return self

    def add_mushrooms(self, mushrooms = False):
        self.mushrooms = mushrooms
        return self

    def add_onions(self, onions = False) :
        self.onions = onions
        return self


    def add_bacon(self, bacon = False):
        self.bacon = bacon
        return self

    def build(self):
        return Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms, self.onions, self.bacon)


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_pizza(self, pizza_name):
        if not self.builder:
            raise ValueError("Please set a builder")
        if pizza_name == "margarita":
            return (self.builder
            .add_size("24cm")
                        .add_cheese(True)
                        .add_mushrooms(True)
                        .build())

        if pizza_name == "pepperoni":
            return (self.builder
            .add_size("32cm")
                        .add_pepperoni(True)
                        .add_cheese(True)
                        .build())

pizza = PizzaDirector(PizzaBuilder())
print(pizza.make_pizza("margarita"))
print(pizza.make_pizza("pepperoni"))


