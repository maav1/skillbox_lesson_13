print('Задача 3. Число наоборот 2')

# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225




def flip_number(number):
        number_reversed = ''
        while number > 0:
                temp = number % 10
                number_reversed += str(temp)
                number //= 10
        return number_reversed
number_one = int(input('Введите первое число: '))
number_one_reversed = flip_number(number_one)
number_two = int(input('Введите второе число: '))
number_two_reversed = flip_number(number_two)
summ_number_reversed = int(number_one_reversed) + int(number_two_reversed)
summ_number = flip_number(summ_number_reversed)
print('\nПервое число наоборот:',number_one_reversed)
print('Второе число наоборот:',number_two_reversed)
print('\nСумма:', summ_number_reversed)
print('Сумма наоборот:',summ_number)