import random
g = 1
f = 1

while f > 0:
    # Получаем входные данные от пользователя и циклично их проверяем на корректность
    while g > 0:
        try:
            volume = (int(input("Введите объем дозы в мл:"))) / 1000
        except (ValueError, NameError):
            print('VolumeError')
            continue

        while g > 0:
            try:
                int1 = int(input("Первая клетка:"))
            except (ValueError, NameError):
                print('int1Error')
                continue

            while g > 0:
                try:
                    int2 = int(input("Вторая клетка:"))
                except (ValueError, NameError):
                    print('int2Error')
                    continue

                while g > 0:
                    try:
                        int3 = int(input("Третья клетка:"))
                    except (ValueError, NameError):
                        print('int3Error')
                        continue


# Получаем  примерное количество клеток
                    bigint = ((int1 + int2 + int2) / 3) * 25

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
