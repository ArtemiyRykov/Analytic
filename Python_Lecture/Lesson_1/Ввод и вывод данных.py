# print() – отвечает за вывод данных
# input() – отвечает за ввод данных

# print('Введите а');
# a = input()
# print('Введите b');
# b = input()
# print(a, b)
# print('{} - {}'.format(a, b))

# print('Введите а');
# a = input() # 10
# print('Введите b');
# b = input() # 20
# c = 30
# print(a, ' + ', b, ' = ', c)

# print('Введите а');
# a = input() # 10
# print('Введите b');
# b = input() # 20
# c = 30
# print(a, ' + ', b, ' = ', c) # 10 + 20 = 30

# print('Введите а');
# a = int(input())
# print('Введите b');
# b = int(input())
# c = 30
# print(a, ' + ', b, ' = ', c)
# print('{} + {} = {}'.format(a, b, c))

# print('Введите а');
# a = float(input())
# print('Введите b');
# b = float(input())
# c = ...
# print(a, ' + ', b, ' = ', c)

# a = int(input('Введите а: ')) # 11 
# b = int(input('Введите b: ')) # 22
# c = 33
# print('{} + {} = {}'.format(a, b, c))

# a = int(input('Введите а: ')) # 11
# b = int(input('Введите b: ')) # 22
# c = 33
# print('{} + {} = {}'.format(a, b, c)) # 11 + 22 = 33

# a = int(input('Введите \nа: '))
# b = int(input('Введите \nb: '))
# c = a + b
# print('{} + {} = {}'.format(a, b, c))

#Выводы
a = 123
b = 1.23
s = 'hello world'
print(a, '-', b, '-', s)
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')