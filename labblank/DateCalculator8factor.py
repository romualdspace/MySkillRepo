# Импорт библиотек
import datetime
from dateutil.relativedelta import relativedelta
from sys import stdin, exit as sys_exit
from colorama import init
from termcolor import colored


a = str('выход')
b = str('exit')
monthCounter = [ai for ai in range(1, 13)]
dayCounter = [bi for bi in range(1, 32)]
yearCounter = [ci for ci in range(1900, 2200)]

while True:
    try:
        dateSelect = input(
            'Дата отбора в формате ДД ММ ГГГГ(разделены пробелами):' '\n    ')
        if a == dateSelect or b == dateSelect:
            sys_exit()
        else:
            dayS, monthS, yearS = map(int, dateSelect.split(' '))
            dateS = datetime.date(day=dayS, month=monthS, year=yearS)
    except (ValueError, NameError):
        print(colored(
            'Дата введена неверно. Проверьте правильность введеной даты.', 'white', 'on_red'))
    if len(dateSelect) == 10 and monthS in monthCounter and dayS in dayCounter and yearS in yearCounter:
        while True:
            try:
                dateRelease = input(
                    'Дата изготовления в формате ДД ММ ГГГГ(разделены пробелами):' '\n    ')
                if a == dateRelease or b == dateRelease:
                    sys_exit()
                else:
                    dayR, monthR, yearR = map(int, dateRelease.split(' '))
                    dateR = datetime.date(day=dayR, month=monthR, year=yearR)

                    if len(dateRelease) == 10 and monthS in monthCounter and dayS in dayCounter and yearS in yearCounter:

                        diffDelta = relativedelta(dateS, dateR)

                        print('-----------------')
                        print(colored('    Год(а):    ', 'blue'), diffDelta.years)
                        print(colored('    Месяца(ев):', 'blue'),
                              diffDelta.months)
                        print(colored('    День(ей):  ', 'blue'),
                              diffDelta.days + 1)
                        print('-----------------')
                        print('Для изменения даты отбора перезапустите программу')
                        print('Для выхода наберите exit или выход')
                        print('=======================================')
                    else:
                        print(colored(
                            'Дата введена неверно. Проверьте правильность введеной даты.', 'white', 'on_red'))
            except (ValueError, NameError):
                print(colored(
                    'Дата введена неверно. Проверьте правильность введеной даты.', 'white', 'on_red'))
    else:
        print(colored(
            'Дата введена неверно. Проверьте правильность введеной даты.', 'white', 'on_red'))
