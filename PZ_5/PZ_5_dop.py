#Задание: Даны три числа. Определить у какого числа больше сумма цифр. Вывод результата предусмотреть в основной программе. Расчет суммы цифр оформить в функции
def NumSum(num):
  total_sum = 0
  for i in str(num):
    total_sum+=int(i)
  return total_sum
 
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
  

    
    
  
