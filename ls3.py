print('Введите два положительных числа')

while True:
    try:
        print("Введите число А")
        a = int(input())
        if a > 0 or a == 0:
            print("Номер А подходит")
            break
        else:
            print("Введите не отрицательное число А")
    except ValueError:
        print("Вы ввели не число!")

while True:
    try:
        print("Введите число Б")
        b = int(input())
        if b > 0 or b == 0:
            print("Номер Б подходит")
            break
        else:
            print("Введите не отрицательное число Б")
    except ValueError:
        print("Вы ввели не число!")

try:
    sum = a + b
    print("sum", sum)
    dif = a - b
    print("dif", dif)
except ZeroDivisionError:
        print("Деление на 0 невозможно, укажите другое число Б")








