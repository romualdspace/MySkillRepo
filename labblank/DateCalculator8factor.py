# Импорт библиотек
import datetime
from dateutil.relativedelta import relativedelta
from sys import stdin, exit as sys_exit
from colorama import init
from termcolor import colored

# Задаем эталонные переменные
a = str('выход')
b = str('exit')
monthCounter = [ai for ai in range(1, 13)]
dayCounter = [bi for bi in range(1, 32)]
yearCounter = [ci for ci in range(1900, 2200)]

# Цикл проверки введенной даты ОТБОРА пробы
while True:
    try:
        dateSelect = input(
            'Дата отбора в формате ДД ММ ГГГГ(разделены точками):' '\n    ')
        if a == dateSelect or b == dateSelect:
            sys_exit()
        else:
            if len(dateSelect) == 10:
                dayS, monthS, yearS = map(int, dateSelect.split('.'))
                if monthS in monthCounter and dayS in dayCounter and yearS in yearCounter:
                    dateS = datetime.date(day=dayS, month=monthS, year=yearS)
                else:
                    raise ValueError
            else:
                raise ValueError

    except (ValueError, NameError):
        print(colored(
            'Дата отбора введена неверно. Проверьте правильность введеной даты.', 'white', 'on_red'))
        continue

# Цикл проверки введенной даты ИССЛЕДОВАНИЯ пробы
    while True:
        try:
            dateRelease = input(
                'Дата изготовления в формате ДД ММ ГГГГ(разделены точками):' '\n    ')
            if a == dateRelease or b == dateRelease:
                sys_exit()
            else:
                if len(dateRelease) == 10:
                    dayR, monthR, yearR = map(int, dateRelease.split('.'))
                    if monthR in monthCounter and dayR in dayCounter and yearR in yearCounter:
                        dateR = datetime.date(
                            day=dayR, month=monthR, year=yearR)

#Вычисление разницы дат
                        diffDelta = relativedelta(dateS, dateR)

                        print('-----------------')
                        print(colored('    Год(а):    ', 'blue'),
                              diffDelta.years)
                        print(colored('    Месяца(ев):', 'blue'),
                              diffDelta.months)
                        print(colored('    День(ей):  ', 'blue'),
                              diffDelta.days + 1)
                        print('-----------------')
                        print(
                            'Для изменения даты отбора перезапустите программу')
                        print('Для выхода наберите exit или выход')
                        print('=======================================')
                    else:
                        raise ValueError
                else:
                    raise ValueError
        except (ValueError, NameError):
            print(colored(
                'Дата изготовления введена неверно. Проверьте правильность введеной даты.', 'white', 'on_red'))