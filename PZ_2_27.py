# Задача: определить сколько секунд прошло за последний час
try:
    n = int(input("Введите количество прошедших секунд за день:"))
    seconds_hour = 3600
    seconds_last_hour = n % seconds_hour
    print(seconds_last_hour)
except ValueError:
    print("Ошибка! Введите целое число")
