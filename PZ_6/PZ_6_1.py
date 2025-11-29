#Задание: Дан список A размера N. Найти минимальный элемент из его элементов с четными номерами A2, A4, A6...
try:
    n=int(input('введите количестов элементов списка:'))
    a=list()
    min_el = None
    for i in range(n):
        b=int(input(f"введите элемент {i}"))
        a.append(b)
    for i in range(0,n,2):
        if min_el is None or a[i]<min_el:
            min_el = a[i]
    print(f"минимальный элемент: {min_el}")
except ValueError:
    print("Ошибка! Введите целое число!")
