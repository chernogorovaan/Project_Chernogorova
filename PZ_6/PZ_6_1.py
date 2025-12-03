#Задание: Дан список A размера N. Найти минимальный элемент из его элементов с четными номерами A2, A4, A6...
import random
try:
    n=random.randint(1,1000)
    a=list()
    min_el = None
    for i in range(n):
        b=random.randint(1,1000)
        a.append(b)
    for i in range(0,n,2):
        if min_el is None or a[i]<min_el:
            min_el = a[i]
    print(f"минимальный элемент: {min_el}")
except ValueError:
    print("Ошибка! Введите целое число!")
