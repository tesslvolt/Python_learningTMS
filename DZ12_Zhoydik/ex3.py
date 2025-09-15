# Класс «Автобус». Класс содержит свойства:
# ● скорость
# ● максимальное количество посадочных мест
# ● максимальная скорость
# ● список фамилий пассажиров
# ● флаг наличия свободных мест
# ● словарь мест в автобусе
# Методы:
# ● посадка и высадка одного или нескольких пассажиров
# ● увеличение и уменьшение скорости на заданное значение
# ● операции in, += и -= (посадка и высадка пассажира по
# фамилии

class Bus:
    def __init__(self, max_seats: int, max_speed: int):
        self.__speed = 0
        self.__max_seats = max_seats
        self.__max_speed = max_speed
        self.__passengers: list[str] = []
        self.__seats: dict[int, str] = {}
        self.__has_free_seats = True

    def board(self, passengers: list[str]):
        for p in passengers:
            if len(self.__passengers) < self.__max_seats:
                seat_number = len(self.__passengers) + 1
                self.__passengers.append(p)
                self.__seats[seat_number] = p
            else:
                self.__has_free_seats = False
                print(f"Нет свободных мест для {p}")
        self.__has_free_seats = len(self.__passengers) < self.__max_seats

    def disembark(self, passengers: list[str]):
        for p in passengers:
            if p in self.__passengers:
                self.__passengers.remove(p)
                # удаляем из словаря места
                for seat, name in list(self.__seats.items()):
                    if name == p:
                        del self.__seats[seat]
                        break
        self.__has_free_seats = len(self.__passengers) < self.__max_seats

    def change_speed(self, value: int):
        self.__speed = max(0, min(self.__max_speed, self.__speed + value))

    def __contains__(self, name: str) -> bool:
        return name in self.__passengers

    def __iadd__(self, name: str):
        self.board([name])
        return self

    def __isub__(self, name: str):
        self.disembark([name])
        return self

    def __str__(self):
        return (f"Скорость: {self.__speed}/{self.__max_speed}, "
                f"Пассажиры ({len(self.__passengers)}/{self.__max_seats}): {self.__passengers}, "
                f"Свободные места: {self.__has_free_seats}")

bus = Bus(max_seats=3, max_speed=90)

bus.board(["саша", "петя"])
print(bus)

bus += "миша"
print(bus)

print("петя" in bus)
print("миша" in bus)

bus -= "саша"
print(bus)

bus.change_speed(50)
print(bus)

bus.change_speed(100)
print(bus)

bus.change_speed(-200)
print(bus)
