list = [5, 6, 7, 1, 2, 3, 4]

end_of_list = (list.index(max(list))) + 1
list1 = list[:end_of_list:]

stat_list = (list.index(min(list)))
list2 = list[stat_list::]

print(list1)
print(list2)

def binary_search(list1, number1):
    if True:
        first = 0
        last = len(list1) - 1
        while last >= first:
            mid = (first + last) // 2
            if list1[mid] == number1:
                return True
            else:
                if list1[mid] > number1:
                    last = mid - 1
                else:
                    first = mid + 1
        else:
            first = 0
            last = len(list2) - 1
            while last >= first:
                mid = (first + last) // 2
                if list2[mid] == number1:
                    return True
                else:
                    if list1[mid] > number1:
                        last = mid - 1
                    else:
                        first = mid + 1

number = int(input("Введите число для поиска: "))

print(binary_search(list1, number))