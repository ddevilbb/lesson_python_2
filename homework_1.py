"""Практическое задание 1"""
print('Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.')
while True:
    try:
        inputString = input('Введите число: ')
        number = inputString.replace('.', '').replace(',', '')
        if not number.isdigit():
            raise ValueError
        result = 0
        for i in number:
            result += int(i)
        print(f'{inputString} -> {result}')
        break
    except ValueError:
        print('Допустимые значения: любое вещественное число(примеры: \'1\', \'1.23\', \'1,23\')')
