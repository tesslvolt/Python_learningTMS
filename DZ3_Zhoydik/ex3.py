'''
Дана строка, состоящая из слов, разделенных пробелами. (Вот 4
варианта тестовых данных для программы: ‘Hello world’, ‘a b c’, ‘test’,
‘test1 test2 test3 test4 test5’). Определите, сколько в ней слов.
'''

string = ("test1 test2 test3 test4 test5")
space_quantity = string.count(" ") + 1
print("Количество слов:", space_quantity)