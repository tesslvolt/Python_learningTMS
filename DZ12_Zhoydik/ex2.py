# ПчёлоСлон
# Экземпляр класса инициализируется двумя целыми числами,
# первое относится к пчеле, второе – к слону. Класс реализует
# следующие методы:
# ● fly() – возвращает True, если часть пчелы не меньше части
# слона, иначе – False
# ● trumpet() – если часть слона не меньше части пчелы,
# возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
# ● eat(meal, value) – может принимать в meal только ”nectar”
# или “grass”. Если съедает нектар, то value вычитается из
# части слона, пчеле добавляется. Иначе – наоборот. Не
# может увеличиваться больше 100 и уменьшаться меньше 0.

class BeeElephant:
    def __init__(self, bee: int, elephant: int):
        self.__bee = bee
        self.__elephant = elephant

    def fly(self) -> bool:
        return self.__bee >= self.__elephant

    def trumpet(self) -> str:
        if self.__elephant >= self.__bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal: str, value: int):
        if meal == "nectar":
            self.__bee = min(100, self.__bee + value)
            self.__elephant = max(0, self.__elephant - value)
        elif meal == "grass":
            self.__elephant = min(100, self.__elephant + value)
            self.__bee = max(0, self.__bee - value)
        else:
            raise ValueError("meal must be 'nectar' or 'grass'")

    def __str__(self):
        return f"Bee: {self.__bee}, Elephant: {self.__elephant}"


c = BeeElephant(40, 60)

print(c)
c.eat("nectar", 30)
print(c)

c.eat("grass", 50)
print(c)

print(c.fly())
print(c.trumpet())