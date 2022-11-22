# 2.Напишите программу, которая будет принимать
# на вход дробь и показывать первую цифру дробной части
# числа.*Примеры: *
# - 6, 78 -> 7
# - 5 -> нет
# - 0, 34 -> 3

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            comment1 = not (x or y or z)
            comment2 = not x and not y and not z
            print(x, y, z, comment1, comment2)
