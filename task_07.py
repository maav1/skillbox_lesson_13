print('Задача 7. Маятник ')

# Известно, что амплитуда качающегося маятника с каждым разом затухает
# на 8,4% от амплитуды прошлого колебания. 
# Если качнуть маятник,
# то, строго говоря, он не остановится никогда, 
# просто амплитуда будет постоянно уменьшаться до тех пор, 
# пока мы не сочтём такой маятник остановившимся. 
 
# Напишите программу, 
# определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится. 
 
# Программа получает на вход
# начальную амплитуду колебания в сантиметрах 
# и конечную амплитуду его колебаний,
# которая считается остановкой маятника. 

# Обеспечьте контроль ввода.

# Пример:

# Введите начальную амплитуду: 1
# Введите амплитуду остановки: 0.1
 
# Маятник считается остановившимся через 27 колебаний


attenuation = 0.084
number_oscilation = 0
initial_amplitude = int(input('Введите начальную амплитуду: '))
stop_amplitude = float(input('Введите амплитуду остановки: '))
if initial_amplitude > stop_amplitude:
  initial_amplitude -= attenuation
  number_oscilation += 1
  print(initial_amplitude,'-',number_oscilation) 