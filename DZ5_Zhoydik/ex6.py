numbers = [4, 6, 2, 8, 5, 3]
numbers_sorted = sorted(numbers)

print("Отсортированный список", numbers_sorted)

def binary_search(numbers_sorted, number):
    first = 0
    last = len(numbers_sorted) - 1
    while last >= first:
        mid = (first + last) // 2
        if numbers_sorted[mid] == number:
            return True

        else:
            if numbers_sorted[mid] > number:
                last = mid - 1
            else:
                first = mid + 1
    return False

number = int(input("Введите число для поиска: "))

print(binary_search(numbers_sorted, number))
if number in numbers:
    print("позиция в исходном списке", numbers.index(number))
else:
    print("такого числа в исходном списке нету")

