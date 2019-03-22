import random

# Задаем входящие параметры
volume = (int(input("Введите объем дозы в мл:"))) / 1000
int1 = int(input("Первая клетка:"))
int2 = int(input("Вторая клетка:"))
int3 = int(input("Третья клетка:"))

# Получаем  примерное количество клеток
bigint = ((int1 + int2 + int2) / 3) * 25

# Производим расчет количества клеток в каждой из 25 клеток
analog = bigint
counter = 25
list = []
while counter > 0:
    percent = random.randint(1, 25)
    pluscorrect = (bigint / 25) + (((bigint / 25) / 100) * percent)
    minuscorrect = (bigint / 25) - (((bigint / 25) / 100) * percent)
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
