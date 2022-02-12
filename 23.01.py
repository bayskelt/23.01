# import random
from random import *
# import math
from math import *

# task_1
print('task_1')

a = int(input('Ввести ціле число: '))
b = float(input('Ввести дійсне число: '))
s = (5 * a ** 2 + sqrt(b ** 5 + 2 * a)) / (abs(2 * b + 7) - factorial(4))
print('s =', s)
print('s заокруглене =', round(s, 3))
print('Найближчі цілі числа до s ', floor(s), ' і ', ceil(s))

# task_2
print()
print('task_2')

A = int(input('Введіть число a: '))
B = int(input('Введіть число b: '))
sum_ = sum([random(), uniform(-5, 15), randint(A, B)])
print('Сума =', sum_)
print('Середнє арифметичне =', sum_ / 3)
