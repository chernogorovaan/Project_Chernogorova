#Задание: Составить программу, в которой функция генерирует четырехзначное число и определяет есть ли в числе одинаковые цифры
import random
try:
  def NumbersGen():
    num=random.randint(1000,9999)
    d1=num//1000
    d2=(num//100)%10
    d3=(num//10)%10
    d4=num%10
    if d1==d2 or d1==d3 or d1==d4 or d2==d3 or d2==d4 or d3==d4:
      print('True')
      print(num)
    else:
      print('False')
      print(num)

except ValueError:
    print('Ошибка! Введите цифру')
NumbersGen()


