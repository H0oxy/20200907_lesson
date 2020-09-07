print('Сложение двух чисел')
num1 = 5
num2 = 6
sum = num1 + num2
print(sum)

print('Самогенерирующийся пример сложения')
import random
a = random.randint(1, 99)
b = random.randint(2, 98)
c = a + b
print(a, '+' b, '=' c)