#Задание: Дан символ C и строка S. Удвоить каждое вхождение символа C в строку S
c = input('Введите символ c')
s = input('Введите стриоку s')
new_s = ""
for i in s:
  if i==c:
    new_s+=i*2
  else:
    new_s+=i
  print(new_s)
    
