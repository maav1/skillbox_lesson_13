print('Задача 5. Число Эйлера')

# Напишите программу, которая находит сумму  ряда с точностью до 1e-5.

# P.S: Формулу смотреть на сайте :)

# Пример:

# Точность: 1e-20
# Результат: 2.7182818284590455


import math

precision = float(input('Точность: '))
member = 1
i =0
summ_members = 0
while precision < member:
        member = 1/math.factorial(i)
        summ_members += member
        i += 1
print('Результат -',summ_members,' Иттераций -',i)
