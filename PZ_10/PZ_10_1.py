'''
Задание:  Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
последовательности из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Элементы первого и второго файлов:
Элементы первого файла, присутствующие во втором:
Элементы второго файла, присутствующие в первом:
Количество элементов:
Количество отрицательных элементов:
Количество положительных элементов:
'''
numbers1 = [-5, 12, -3, 8, -1, 7, 0, -4, 10]
numbers2 = [3, -5, 7, -2, 8, -9, 4, 0, 15]
f1 = open('file1.txt', 'w')
f2 = open('file2.txt', 'w')

for i in numbers1:
    f1.write(str(i) + ' ')
for i in numbers2:
    f2.write(str(i) + ' ')
f1.close()
f2.close()

f1 = open('file1.txt', 'r')
f2 = open('file2.txt', 'r')
a = []
b = []
for x in f1.read().split(): a.append(int(x))
for x in f2.read().split(): b.append(int(x))
f1.close()
f2.close()


all = a + b
common1 = []
common2 = []
neg = 0
pos = 0

for x in a:
    if x in b: common1.append(x)
for x in b:
    if x in a: common2.append(x)
for x in all:
    if x < 0: neg += 1
    if x > 0: pos += 1

r = open('result.txt', 'w')
r.write('Элементы первого и второго файлов:\n' + str(a) + '\n' + str(b) + '\n\n')
r.write('Элементы первого файла, присутствующие во втором:\n' + str(common1) + '\n\n')
r.write('Элементы второго файла, присутствующие в первом:\n' + str(common2) + '\n\n')
r.write('Количество элементов:\n' + str(len(all)) + '\n\n')
r.write('Количество отрицательных элементов:\n' + str(neg) + '\n\n')
r.write('Количество положительных элементов:\n' + str(pos))
r.close()
