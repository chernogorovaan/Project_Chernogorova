'''
Составить генератор (yield), который переведет символы строки из нижнего
регистра в верхний.
'''
def uppercase_f (s):
    for i in s:
        yield i.upper()

stroka = input('Введите строку')
result = ''
for i in uppercase_f(stroka):
    result+=i
print(result)
