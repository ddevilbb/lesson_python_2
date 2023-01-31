"""Практическое задание 2"""
print('Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.')
while True:
    try:
        N = int(input('Введите число N: '))
        if N < 1:
            raise ValueError
        result = 1
        for i in range(1, N + 1):
            result *= i
            if i < N:
                print(result, end=', ')
            else:
                print(result)
        break
    except ValueError:
        print('Допустимые значения: любое целое число больше 1')
