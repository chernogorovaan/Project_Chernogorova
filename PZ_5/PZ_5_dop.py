#Задание: Даны три числа. Определить у какого числа больше сумма цифр. Вывод результата предусмотреть в основной программе. Расчет суммы цифр оформить в функции
def NumSum(num):
  n1 = num//100
  n2 = (num//10)%10
  n3 = num%10
  return n1+n2+n3
 
def Numbers():
  a=int(input(':'))
  b=int(input(':'))
  c=int(input(':'))
  sum1=NumSum(a)
  sum2=NumSum(b)
  sum3=NumSum(c)
  if sum1>sum2 and sum1>sum3:
    print(sum1)
  elif sum2>sum1 and sum2>sum3:
    print(sum2)
  elif sum3>sum1 and sum3>sum2:
    print(sum3)

#Задание: Расчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в функции
def PerimS():
  a = int(input())
  b = int(input())
  p = (a+b)*2
  s = a*b
  print(p)
  print(s)

PerimS()

#Задание: Написать программу, подсчитывающую количество цифр числа, используя для этого функцию
def SymCount():
    num = int(input(':'))
    count = 0
    while num>0:
        count+=1
        num=num//10
    print(count)
SymCount()


    
    
  
