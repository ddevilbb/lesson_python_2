"""Практическое задание 3"""
print('Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.')
while True:
    try:
        n = int(input('Введите число n: '))
        if n < 1:
            raise ValueError
        result = 0
        for i in range(1, n + 1):
            number = round(((1 + 1/i)**i), 2)
            result += number
            if i < n:
                print(number, end=' + ')
            else:
                print(number, end=' = ')
        print(result)
        break
    except ValueError:
        print('Допустимые значения: любое целое число больше 1')
