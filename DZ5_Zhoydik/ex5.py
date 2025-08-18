numbers = [1, 2, 1, 4, 5]
dup_elements = {}

for number in numbers:
    if number in dup_elements:
        dup_elements[number] += 1
    else:
        dup_elements[number] = 1

print(dup_elements)

