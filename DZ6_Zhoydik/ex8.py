# Реализовать функцию, которая находит минимальный и
# максимальный элементы в матрице (матрица M x N). Вывести
# в консоль индексы найденных элементов.
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6,], [7, 8, 9]])

print(matrix)

def searching_elements(matrix):
    a =  np.min(matrix)
    b = np.max(matrix)
    print(f" наименьший элемент {a}, наибольший элемент {b}")
    i, j = np.where(matrix == a)
    print("координаты наименьшего элемента: ", i, j)
    i, j = np.where(matrix == b)
    print("координаты наибольшего элемента", i, j)

searching_elements(matrix)






