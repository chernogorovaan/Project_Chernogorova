#Задание: Найти и вывести на экран сумму и количество отрицательных чисел.
for i in range(4):
  a=int(input(':'))
  i=0
  sum=0
  if a>0:
    i+=1
    sum+=a
print(i)
print(sum)

#Задание: Ввести 4 числа. Найти и вывести на экран количество четных чисел.
for i in range(4):
  a=int(input(':'))
  i=0
  if a%2==0:
    i+=1
    sum+=a
print(i)

#Задание: Найти и вывести на экран квадраты и кубы чисел от 2 до 5.
for i in range (2,5):
  a=i**2
  b=i**3
  print(a)
  print(b)

#Задание: Найти и вывести на экран S=1!+2!+3!+...+n! (n>1).
n=int(input(':')
if n<=1:
      print('n должно быть больше 1!')
else:
  s = 0
  fact = 1
  for i in range(1, n + 1):
    fact * = i
    s += fact
print(f'S = 1! + 2! = ... + {n}! = {s}')

#Задание: Ввести N чисел. Найти и вывести их среднее арифметическое
n = int(input(':'))
if n<=0:
  print('Количество должно быть положительным числом!')
else:
  sum = 0
  print (f'Введите {n} чисел!')
  for i in range(n):
    n=int(input(':'))
    sum+=n


