import random
'''
print('Сложение двух чисел')
num1 = 5
num2 = 6
sum = num1 + num2
print(sum)
'''

#print('Самогенерирующийся пример сложения')
#a = random.randint(1, 99)
#b = random.randint(2, 98)
#c = a + b
#print(a, '+', b, '=', c)

a = random.randint(1, 99)
b = random.randint(2, 98)
print('Choose operation: add(+), minus(-), multiplication(*), division(/)')
operation = (input())
if operation == "+":
    c = a + b
    print(a, '+', b, '=', c)

if operation == "-":
    c = a - b
    print(a, '-', b, '=', c)

if operation == "*":
    c = a * b
    print(a, '*', b, '=', c)

#Если у числа n-ое кол-во знаков после запятой, то надо сделать меньше
if operation == "/":
    c = a / b
    print(a, '/', b, '=', c)

#Выводит в любом случае, даже если введен "-" или "+", и тому подобное
#else:
#    print('Please enter a correct operation')
