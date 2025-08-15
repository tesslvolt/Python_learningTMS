'''
Дана строка. Замените в этой строке все появления буквы h на
букву H, кроме первого и последнего вхождения.
Подсказка: использовать метод replace с параметрами.
Например, дано: ‘hhhabchghhh’, должно быть: ‘hHHabcHgHHh’
'''

string = ("hhhabchghhh")

first_h = string[:1]
print(first_h)

without = string[1:10]
print(without)

end_h = string[10:]
print(end_h)

new_string = without.replace("h", "H")
print("Новая строка", first_h + new_string + end_h )

