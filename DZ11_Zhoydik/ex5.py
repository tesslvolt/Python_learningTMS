# Разработать класс SuperStr, который наследует
# функциональность стандартного типа str и содержит два
# новых метода:
# ● метод is_repeatance(s), который принимает некоторую
# строку и возвращает True или False в зависимости от того,
# может ли текущая строка быть получена целым
# количеством повторов строки s. Считать, что пустая
# строка не содержит повторов
# ● метод is_palindrom(), который возвращает True или False в
# зависимости от того, является ли строка палиндромом вне
# зависимости от регистра. Пустую строку считать
# палиндромом.
class SuperStr(str):
    def __init__(self, string):
        self.string = string

    def is_rep(self, s):
        if s != "":
            len(self.string) / len(s)
            if s * 3 == self.string:
                print("все норм")
            else:
                print("не совпадает")
        else:
            print("строка пустая!")



    def is_pol(self):
        a = self.string.lower()
        if self.string.replace(" ", "").lower() == a.replace(" ", "")[::-1]:
            print("палиндром")
        else:
            print("не палиндром")


sup = SuperStr("лёша на полке клопа нашёл")
sup.is_rep("лох")
sup.is_pol()



