'''
Дан прямоугольный треугольник с катетами cat_a и cat_b. Найти
площадь треугольника и его гипотенузу.
'''

cat_a = int(input("введите первый катет:"))
while cat_a <= 0:
    cat_a = int(input("Введите число больше нуля:"))
    if cat_a > 0:
        break

cat_b = int(input("введите второй катет:"))
while cat_b <= 0:
    cat_a = int(input("Введите число больше нуля:"))
    if cat_b > 0:
        break

square = (cat_a * cat_b) / 2
hypotenuse = (cat_a ** 2 + cat_b ** 2) ** 0.5

print(square, hypotenuse)
