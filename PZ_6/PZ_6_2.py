"""
Задание: Дан целочисленный список A размера N. 
Переписать в новый целочисленный список B все четные числа из исходного списка (в том же порядке)
 и вывести размер полученного списка B и его содержимое.
"""
import random
try:
    a = []
    n = random.randint(1,1000)
    b = []
    for i in range(n):
        a_el = random.randint(1,1000)
        a.append(a_el)
    for i in a:
        if i%2==0:
            b.append(i)
    print(f"Длина списка b: {len(b)}")
    print(b)
        
except ValueError:
    print("Ошибка! Введите целое число!")
