# Класс «Товар» содержит следующие закрытые поля:
# ● название товара
# ● название магазина, в котором подаётся товар
# ● стоимость товара в рублях
# Класс «Склад» содержит закрытый массив товаров.
# Обеспечить следующие возможности:
# ● вывод информации о товаре со склада по индексу
# ● вывод информации о товаре со склада по имени товара
# ● сортировка товаров по названию, по магазину и по цене
# ● перегруженная операция сложения товаров по цене

from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:
    __name: str
    __shop: str
    __price: float

    # Геттеры
    def get_name(self) -> str:
        return self.__name

    def get_shop(self) -> str:
        return self.__shop

    def get_price(self) -> float:
        return self.__price

    def __str__(self):
        return f"Товар: {self.__name}, Магазин: {self.__shop}, Цена: {self.__price} руб."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.__price + other.__price
        return NotImplemented

@dataclass
class Warehouse:
    __products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product):
        self.__products.append(product)

    def get_product_info_index(self, x: int):
        if x < 0 or x >= len(self.__products):
            print(f"ведите номер от 0 до {len(self.__products)}")
        else:
            print(self.__products[x])

    def get_product_info_name(self, enter_name: str):
        for product__name in self.__products:
            if product__name.get_name().lower() == enter_name.lower():
                print(f"Магазин: {product__name.get_shop()}, Цена: {product__name.get_price()}")


    def get_product_info_price(self):
        print(self.__products)

    def sorted_name(self):
        self.__products.sort(key=lambda x: x.get_name())


    def sorted_price(self):
        h = str(input("Введите фильтр (^ - возрастание, v - убывание): "))
        if h == "^":
           self.__products.sort(key=lambda x: x.get_price(), reverse=False)
        elif h == "v":
            self.__products.sort(key=lambda x: x.get_price(), reverse=True)

    def sorted_shop(self):
        self.__products.sort(key=lambda x: x.get_shop())

    def show_all(self):
        return "\n".join(str(p) for p in self.__products)

w = Warehouse()

w.add_product(Product("Хлеб", "Корона", 45))
w.add_product(Product("Молоко", "Гиппо", 80))
w.add_product(Product("Сыр", "Санта", 350))
w.get_product_info_name("молоко")
w.sorted_price()
print(w.show_all())

p1 = Product("Яблоки", "Рынок", 120)
p2 = Product("Виноград", "Евроопт", 200)
print("Сумма цен:", p1 + p2)  # 320
