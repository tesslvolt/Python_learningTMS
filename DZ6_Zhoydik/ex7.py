# Реализовать функцию, которая создаёт матрицу
# размером M строк на N столбцов и заполняет её рандомными
# числами.
import random

def create_matrix(M, N, min_val=0, max_val=100):
    matrix = []
    for i in range(M):
        row = [random.randint(min_val, max_val) for _ in range(N)]
        matrix.append(row)
    return matrix

M = int(input("Введите количество m: "))
N = int(input("Введите количество n: "))

matrix = create_matrix(M, N)

print("матрица:")
for row in matrix:
    print(row)