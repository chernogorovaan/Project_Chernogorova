#Задача: по введенному номеру месяца определить время года
try:
    month = int(input('Введите номер месяца (1-12):'))
    if month<1 or month>12:
        print('Введите число от 1 до 12')
    else:
        if month==1 or month==2 or month==12:
            print('Зима')
        elif 3<=month<=5:
            print('Весна')
        elif 6<=month<=8:
            print('Лето')
        else:
            print("Осень")
except ValueError:
    print("Ошибка! Введите целое число от 1 до 12")
