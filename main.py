mport random
import math

#Задача 1
m = math
x = int(input('Введіть значення x  '))
y = float(input('Введіть значення y  '))
z = (m.sqrt(6 * x**6 - 5)-3 * y**2)/(m.factorial(5) - abs(2+y))

#Задача 2
print(z)
print(round(z, 4))
print('Найближче більше цільше число', m.ceil(z))
print('Найближче менше ціле число', m.floor(z))

#Задача 3
r = random
a = int(input('Введіть число a  '))
b = int(input('Введіть число b  '))
c = r.random()
d = r.uniform(a, b)
e = r.randint(2, 20)
result = m.sqrt(c*d*e)
print(result)
