try:
    N = int(input("Введите число N (>0): "))
    if N <= 0:
        print("Ошибка: N должно быть больше 0")
    else:
        total_sum = 0
        for i in range(1, N + 1):
            total_sum += 1 / i
        print(f"Сумма 1 + ... + 1/{N} = {total_sum}")
    
except ValueError:
    print("Ошибка: Введите целое число!")
