# Импорт библиотек
import datetime
from dateutil.relativedelta import relativedelta
from sys import stdin, exit as sys_exit
from colorama import init
from termcolor import colored


a = str('exit')

# Получаем от пользователя строки дат
dateSelect = input(
    'Дата отбора в формате ДД ММ ГГГГ(разделены пробелами):' '\n')

# Циклический ввод даты изготовления
while True:
    try:
        dateRelease = input(
            'Дата изготовления в формате ДД ММ ГГГГ(разделены пробелами):' '\n')
        if dateRelease == a:
            sys_exit()
        else:
            # Рассортировываем полученные даты по переменным
            dayS, monthS, yearS = map(int, dateSelect.split(' '))
            dayR, monthR, yearR = map(int, dateRelease.split(' '))

# Преобразуем полученные переменные в тип datetime
            dateS = datetime.date(day=dayS, month=monthS, year=yearS)
            dateR = datetime.date(day=dayR, month=monthR, year=yearR)

# Производим вычисление
            diffDelta = relativedelta(dateS, dateR)

# Результат
            print(colored('Год(а): ', 'blue'), diffDelta.years)
            print(colored('Месяцев:', 'blue'), diffDelta.months)
            print(colored('Дней:   ', 'blue'), diffDelta.days + 1)
            print('=======================================')
            print('Для изменения даты отбора перезапустите программу')
            print('Для выхода наберите exit')
            print('=======================================')
    except ValueError:
        print(colored(
            'Дата введена неверно. Перепроверьте правильность введеной даты.', 'white', 'on_red'))
