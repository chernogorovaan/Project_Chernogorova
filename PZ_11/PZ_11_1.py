"""
Звдание: В последовательности их N чисел (N –четное) в первой ее половине найти
произведение элементов меньших 0.
"""
import random
n = []
for i in range (10):
    i=random.randint(-10,10)
    n.append(i)
half = n[:len(n)//2]
neg = [i for i in half if i<0]
total = 1
for i in neg:
    total = total * i
print(total)
print(neg)
print(n)
print(half)
