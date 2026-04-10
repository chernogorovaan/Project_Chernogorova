'''
2. В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.
'''
import random
matrix = [[random.randint(1, 20) for _ in range(3)] for _ in range(3)]

print("Исходная матрица:")
print(*matrix, sep='\n')

try:
    n = int(input("\nВведите номер строки для изменения (0, 1 или 2): "))
    
    
    if 0 <= n < len(matrix):
        matrix[n] = [element + 3 for element in matrix[n]]

        print("\nМатрица после изменения:")
        print(*matrix, sep='\n')
    else:
        print(f"Ошибка: В матрице нет строки с номером {n}. Доступны строки 0, 1 и 2.")

except ValueError:
    print("Ошибка: Нужно ввести целое число.")