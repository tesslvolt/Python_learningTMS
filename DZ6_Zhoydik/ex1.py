# Дан список чисел, отсортированных по возрастанию.
# На вход принимается значение, равное одному из элементов
# списка. Реализовать функцию, выполняющую рекурсивный
# алгоритм бинарного поиска, на выходе программа должна
# вывести позицию искомого элемента в исходном списке.
list = [7, 4, 5, 3, 2, 1]
sorted_list = sorted(list)

def binarySearch(sorted_list, item, low = 0, high = None):

    if high is None:
        high = len(sorted_list) - 1

    while (low <= high):
        mid = (low + high) // 2 #2
        if sorted_list[mid] == item:
            return mid
        elif sorted_list[mid] > item:
            return binarySearch(sorted_list, item, low, mid - 1)
        else:
            return binarySearch(sorted_list, item, mid + 1, high)
        return False

x = int(input("Введите искомое число: "))

i = 0

for item in list:
    if item == x:
        break
    else:
        i += 1

if i == len(list):
    print("Такого числа в списке нету!")
    in_first_list = None
else:
    in_first_list = list.index(x)

result =  binarySearch(sorted_list, x)

print(f"Вы ввели число {x}, позиция элемента в отсортированном списке: {result},\n"
      f"позиция элемента в изначальном списке: {in_first_list} ")