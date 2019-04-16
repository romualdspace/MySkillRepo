#-*- coding: utf-8 -*-
'''
Калькулятор дат предназначени для рассчета разницы дат хранения компонентов крови нашей лаборатории.
'''

# Импорт библиотек
from sys import exit as sys_exit
import datetime
from dateutil.relativedelta import relativedelta
from termcolor import colored

# Задаем эталонные переменные
a = str('выход')
b = str('exit')
monthCounter = [ai for ai in range(1, 13)]
dayCounter = [bi for bi in range(1, 32)]
yearCounter = [ci for ci in range(1900, 2200)]

#Функции

def wish_exit(x):
    if x in (a, b):
        sys_exit()

def good_input(x):
    if len(x) != 10:
        raise ValueError

def mapper(x):
    dayM, monthM, yearM = map(int, x.split('.'))
    return dayM, monthM, yearM


def dater(dayM, monthM, yearM):
    if dayM in dayCounter and monthM in monthCounter and yearM in yearCounter:
        date = datetime.date(day=dayM, month=monthM, year=yearM)
        return date


def diff(a, b):
    diffDelta = relativedelta(dateS, dateR)

    print('-----------------')
    print(colored('    Год(а):    ', 'blue'), diffDelta.years)
    print(colored('    Месяца(ев):', 'blue'), diffDelta.months)
    print(colored('    День(ей):  ', 'blue'), diffDelta.days + 1)
    print('-----------------')
    print('Для изменения даты отбора перезапустите программу')
    print('Для выхода наберите exit или выход')
    print('=======================================')



while True:
    try:
        dateSelect = input(
            'Дата отбора в формате ДД.ММ.ГГГГ(разделены точками):' '\n    ')
        wish_exit(dateSelect)
        good_input(dateSelect)
        dayS, monthS, yearS = map(int, mapper(dateSelect))
        dateS = dater(dayS, monthS, yearS)
    except (ValueError, NameError):
        print(colored(
            'Дата ошибочна. Проверьте правильность введеной даты.', 'white', 'on_red'))
        continue

    while True:
        try:
            dateRelease = input(
                'Дата изготовления в формате ДД.ММ.ГГГГ(разделены точками):' '\n    ')
            wish_exit(dateRelease)
            good_input(dateRelease)
            dayR, monthR, yearR = map(int, mapper(dateRelease))
            dateR = dater(dayR, monthR, yearR)
        except (ValueError, NameError):
            print(colored(
                'Дата ошибочна. Проверьте правильность введеной даты.', 'white', 'on_red'))
            continue

        diff(dateS, dateR)
