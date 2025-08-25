# Программа получает на вход число H. Реализовать
# функцию, которая определяет, какие столбцы имеют хотя бы
# одно такое же число, а какие не имеют (матрица M x N).
import numpy as np

matrix = np.array([[1, 3, 3], [4, 5, 3,], [7, 8, 9]])

check_number = int(input("Введите число для проверки:"))

def check_col(matrix, number):

    overlap = []

    for i in range(matrix.shape[1]): # .shape[1] указывает на столбцы
        for j in range(matrix.shape[0]): # .shape[0] указывает на строки
            if matrix[j][i] == number:
                overlap.append(matrix[j][i])
        print(f"В столбце {i+1} следующее количество совпадений {len(overlap)}")

check_col(matrix, check_number)


