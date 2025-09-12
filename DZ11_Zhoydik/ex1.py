# Создайте класс Soda (газировка). Для инициализации
# есть параметр, который определяет вкус газировки. При
# инициализации этот параметр можно задавать, а можно и не
# задавать. Реализовать метод строковой репрезентации,
# который возвращает строку вроде «У вас газировка с
# <клубничным> вкусом», если вкус задан. Если вкус не задан,
# метод должен возвращать строку «У вас обычная газировка».

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Book:
    title: str
    year: int

    def __post_init__(self):
        if self.year > date.today().year:
            raise ValueError(f'год не тот')

@dataclass
class Library:
    books: list[Book] = field(default_factory=list)

    def add_book(self, books: Book):
        self.books.append(books)


lib = Library()
lib.add_book(Book("pyt", 1999))
lib.add_book(Book("c++", 1909))
lib.add_book(Book("java", 2012))

print(len(lib.books))
print(lib.books)
# b = Book("Анна", 1999)
# print(b)
