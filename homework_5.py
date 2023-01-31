"""Практическое задание 5"""
import random

print('Реализуйте алгоритм перемешивания списка.')
while True:
    try:
        cnt = int(input('Введите количество элементов списка: '))
        if cnt < 1:
            raise ValueError
        lst = list(range(cnt))
        lstClone = lst[:]
        lstCloneLength = len(lstClone)
        for i in range(lstCloneLength):
            randomIndex = random.randint(0, lstCloneLength - 1)
            tmp = lstClone[i]
            lstClone[i] = lstClone[randomIndex]
            lstClone[randomIndex] = tmp
        print(f'{lst} -> {lstClone}')
        break
    except ValueError:
        print('Допустимые значения: любое целое число больше 1')
