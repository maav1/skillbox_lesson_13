print('Задача 4. Урок информатики 3')

# Наконец-то учитель смог объяснить детям,
# что такое эта «плавающая точка». Однако долго его радость не продлилась,
# ведь на следующем уроке нужно будет объяснить такие страшные слова,
# как «экспоненциальное», «мантисса» и «порядок».

# Хоть старшеклассники и знакомы с экспонентой,
# учитель всё равно не уверен, что здесь всё будет понятно.
# Поэтому для наглядности он также написал программу.

# На вход подаётся строка — это экспоненциальная форма числа.
# Напишите программу,
# которая выводит отдельно мантиссу и отдельно порядок этого числа.


string = input('Введите число в экспоненциальной форме: ')
mantissa = ''
i=0
for symbol in string:
        if symbol != 'e':
                i +=1
                mantissa += symbol
        else:
                break
print('Мантисса:',mantissa,'\nПорядок',string[i+1:])