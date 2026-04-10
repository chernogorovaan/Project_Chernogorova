'''
1. В матрице найти среднее арифметическое положительных элементов, кратных 3.
'''
import random

rows, cols = 3, 3
matrix = [[random.randint(-10,10) for i in range(cols)] for i in range(rows)]
print("Сгенерированная матрица 3x3:")
print(*matrix, sep='\n')

suitable_elements = [element for row in matrix for element in row if element > 0 and element % 3 == 0]

result = sum(suitable_elements) / len(suitable_elements) if suitable_elements else None

print("\nСреднее арифметическое положительных элементов, кратных 3:", result)