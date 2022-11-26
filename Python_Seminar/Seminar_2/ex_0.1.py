# округление

numbers = input('Введите число:')
count = int(input('Введите точность: '))
print(numbers)
numbers = numbers.split('.')  # split()  разбиваем и создает список
print(numbers)

print(float(numbers[0] + '.' + numbers[1][0:count]))
