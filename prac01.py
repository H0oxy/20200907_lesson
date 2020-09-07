'''
print('Сложение двух чисел')
num1 = 5
num2 = 6
sum = num1 + num2
print(sum)
'''

import random

print('Самогенерирующийся пример сложения')
a = random.randint(1, 99)
b = random.randint(2, 98)
c = a + b
print(a, '+', b, '=', c)

print('Change operation: add(+), minus(-), multiplication(*), division(/)')
operation = int(input('+,-.*,/.'))
if operation == "+":
    print(a, operatiom, b, '=', c)
    else:
    print('Please enter a correct operation')
if operation == "-":
    print(a, operatiom, b, '=', c)
    else:
    print('Please enter a correct operation')
if operation == "*":
    print(a, operatiom, b, '=', c)
    else:
    print('Please enter a correct operation')
if operation == "/":
    print(a, operatiom, b, '=', c)
    else:
    print('Please enter a correct operation')
