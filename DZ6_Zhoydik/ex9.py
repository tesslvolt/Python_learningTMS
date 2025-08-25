# Реализовать функцию, которая находит сумму
# элементов матрицы (матрица M x N). Определить, какую долю
# в общей сумме (процент) составляет сумма элементов
# каждого столбца.

import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6,], [7, 8, 9]])

def data_matrix(matrix):
    sum_mat = np.sum(matrix)
    print(sum_mat)

    sum_columns = np.sum(matrix, axis=0)

    column1 = int(sum_columns[0] * 100 / sum_mat)
    column2 = int(sum_columns[1] * 100 / sum_mat)
    column3 = int(sum_columns[2] * 100 / sum_mat)


    print(f"составляющая первого столбца {column1}%")
    print(f"составляющая второго столбца {column2}%")
    print(f"составляющая третьего столбца {column3}%")

data_matrix(matrix)




