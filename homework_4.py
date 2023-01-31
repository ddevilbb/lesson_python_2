"""Практическое задание 4"""
print('Задайте список из N элементов, заполненных числами из промежутка [-N, N]. '
      'Найдите произведение элементов на указанных позициях. '
      'Позиции хранятся в файле file.txt в одной строке одно число.')
while True:
    try:
        N = int(input('Введите N: '))
        if N < 1:
            raise ValueError
        inputList = list(range(-N, N + 1))
        inputListLength = len(inputList) - 1

        # Работа с файлом
        with open('file.txt', 'r') as fp:
            lines = fp.readlines()
            fp.close()

        # Создаём список множителей для более изящного вывода в консоль.
        multiplierList = list()
        multiplicationResult = 1
        for i, line in enumerate(lines):
            multiplierIndex = int(line.strip())
            if multiplierIndex > inputListLength or multiplierIndex < 0:
                continue
            multiplierList.append(inputList[multiplierIndex])
            multiplicationResult *= inputList[multiplierIndex]
        multiplierListLength = len(multiplierList) - 1

        # Выводим результат в консоль. Пример вывода: `-6 * -7 * -9 * -1 * 1 * 10 * -8 * -6 = 181440`
        print(f'list = {inputList}')
        for i, multiplier in enumerate(multiplierList):
            if i < multiplierListLength:
                print(multiplier, end=' * ')
            else:
                print(multiplier, end=' = ')
        print(multiplicationResult)

        break
    except ValueError:
        print('Допустимые значения: любое целое число больше 1')