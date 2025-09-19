# Паттерн «Фабричный метод»
# ● Создайте абстрактный класс Animal, у которого есть
# абстрактный метод speak.
# ● Создайте классы Dog и Cat, которые наследуют от Animal
# и реализуют метод speak.
# ● Создайте класс AnimalFactory, который использует
# паттерн «Фабричный метод» для создания экземпляра
# Animal. Этот класс должен иметь метод create_animal,
# который принимает строку («dog» или «cat») и возвращает
# соответствующий объект (Dog или Cat).
from abc import abstractmethod


class Animal:
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_sound):
        if animal_sound == "dog":
            return Dog()
        elif animal_sound == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal sound")

Animal = AnimalFactory()
d1 = Animal.create_animal("dog")
print(d1.speak())
d2 = Animal.create_animal("cat")
print(d2.speak())




