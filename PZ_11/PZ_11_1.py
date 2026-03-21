"""
Звдание: В последовательности их N чисел (N –четное) в первой ее половине найти
произведение элементов меньших 0.
"""
import random
from functools import reduce
n = [random.randint(-10,10) for i in range(10)]
half = n[:len(n)//2]
neg = [i for i in half if i<0]
total = reduce(lambda x,y: x*y, neg)
print(total)
print(neg)
print(half)
print(n)

