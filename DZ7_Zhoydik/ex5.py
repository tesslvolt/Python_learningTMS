# Используя map() и reduce() посчитать площадь
# квартиры, имея на входе характеристики комнат квартиры.
import functools

rooms = [
{"name": "Kitchen", "length": 6, "width": 4},
{"name": "Room 1", "length": 5.5, "width": 4.5},
{"name": "Room 2", "length": 5, "width": 4},
{"name": "Room 3", "length": 7, "width": 6.3},
]

sq_rooms = list(map(lambda x: x["length"] * x["width"], rooms))
print(sq_rooms)

sq_apart = functools.reduce(lambda x, y: x + y, sq_rooms)

print(f"{sq_apart} кв.м")