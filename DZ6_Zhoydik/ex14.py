#  Дана матрица M x N. Исходная матрица состоит из
# нулей и единиц. Реализовать функцию, которая добавит к
# матрице ещё один столбец, элементы которого делает
# количество единиц в соответствующей строке чётным
import numpy as np

rows = int(input("введите количество строк: "))
cols = int(input("введите количество столбцов: "))

matrix = np.random.randint(0, 2, size=(rows, cols))
print(f"исходная матрица\n {matrix}")

def units_col(matrix):


    unit_or_zero = []

    for j in range(matrix.shape[0]):
        overlap = []  # .shape[0] указывает на строки
        for i in range(matrix.shape[1]):  # .shape[1] указывает на столбцы
            if matrix[j][i] == 1:
                overlap.append(matrix[j][i])
        unit_or_zero.append(len(overlap) % 2)

    last_col = np.array(unit_or_zero).reshape(-1, 1)
    print(f" добавим {unit_or_zero}")

    result_matrix = np.concatenate((matrix, last_col), axis=1)

    print(f"конечный результат\n {result_matrix}")

units_col(matrix)





