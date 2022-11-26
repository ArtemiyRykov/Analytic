# Для натурального n создать список, состоящий из элементов последовательности
# 3*n + 1.
# *Пример:*
# - Для n = 6: ['1: 4', '2: 7', '3: 10', '4: 13', '5: 16', '6: 19']

n = int(input('Введите число: '))
# my_list = [None]*number
my_list = []
for i in range(1, n+1):
    # my_list.append(str(i) + ': ' + str(3*i+1))
    my_list.append(f'{i}: {3*i+1}')
print(my_list)