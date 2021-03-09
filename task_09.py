

print('Задача 9. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

summ_row = every_member = 1
precision = float(input('Введите точность: '))
number = int(input('Введите x: '))

def exponentiation(number,degree):
    number_in_degree = 1
    for _ in range(degree):
        number_in_degree *= number
    return number_in_degree
def factorial(degree):
    factor = 1
    for i in range(1,degree + 1):
        factor *= i
    return factor

degree = 1
while abs(every_member) > precision:
    every_member = exponentiation(-1,degree) * exponentiation(number,2 * degree) / factorial(2 * degree)
    degree += 1
    summ_row += every_member
print('Сумма ряда равна:',summ_row)






























