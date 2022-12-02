# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.


my_list = ['sgsggdfg45ff', 'ewfafeaw345t56', 'wegfwe45465tgf', 'sdger45634tfg']
number = (input('Введите число:'))

for item in my_list:
    for char in item:
        if char == number:
            print(f'Символ {number} присутствует в строке {item}')

