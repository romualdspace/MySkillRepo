import random
from sys import stdin, exit as sys_exit

g = 1
f = 1
a = str('выход')
b = str('exit')

while f > 0:
    # Получаем входные данные от пользователя и циклично их проверяем на корректность
    while g > 0:
        try:
            volume = (input("Введите объем дозы в мл:"))
            if a == volume or b == volume:
                sys_exit()
            else:
                volume = int(volume) / 1000
        except (ValueError, NameError):
            print('VolumeError')
            continue

        while g > 0:
            try:
                firstCell = input("Первая клетка:")
                if a == firstCell or b == firstCell:
                    sys_exit()
                else:
                    firstCell = int(firstCell)
            except (ValueError, NameError):
                print('firstCellError')
                continue

            while g > 0:
                try:
                    secondCell = input("Вторая клетка:")
                    if a == secondCell or b == secondCell:
                        sys_exit()
                    else:
                        secondCell = int(secondCell)
                except (ValueError, NameError):
                    print('secondCellError')
                    continue

                while g > 0:
                    try:
                        thirdCell = input("Третья клетка:")
                        if a == thirdCell or b == thirdCell:
                            sys_exit()
                        else:
                            thirdCell = int(thirdCell)
                    except (ValueError, NameError):
                        print('thirdCellError')
                        continue


# Получаем  примерное количество клеток
                    bigint = ((firstCell + secondCell + thirdCell) / 3) * 25

# Производим расчет количества клеток в каждой из 25 клеток
                    analog = bigint
                    counter = 25
                    list = []
                    while counter > 0:
                        percent = random.randint(1, 25)
                        pluscorrect = (bigint / 25) + \
                            (((bigint / 25) / 100) * percent)
                        minuscorrect = (bigint / 25) - \
                            (((bigint / 25) / 100) * percent)
                        pendulum = random.randint(0, 1)
                        if pendulum == 0:
                            analog = analog - pluscorrect
                            list.append(int(pluscorrect))
                        else:
                            analog = analog - minuscorrect
                            list.append(int(minuscorrect))
                        counter -= 1

# Подсчитываем общее количество клеток
                    total = sum(list)

# Получаем результат
                    result = (total * 2) * volume

                    print(list)
                    print('Итого:', total)
                    print('Результат: %3.0f' % (result))

                    break
                break
            break