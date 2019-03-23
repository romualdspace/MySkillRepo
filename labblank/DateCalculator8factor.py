#Импорт библиотек
import datetime
from dateutil.relativedelta import relativedelta
from sys import stdin, exit as sys_exit

a = str('exit')

#Получаем от пользователя строки дат
dateSelect = input('Дата отбора в формате ДД ММ ГГГГ(разделены пробелами):')

while True:
    dateRelease = input('Дата изготовления в формате ДД ММ ГГГГ(разделены пробелами):')
    if dateRelease == a:
        sys_exit()
    else:
#Рассортировываем полученные даты по переменным
        dayS, monthS, yearS = map(int, dateSelect.split(' '))
        dayR, monthR, yearR = map(int, dateRelease.split(' '))

#Преобразуем полученные переменные в тип datetime
        dateS = datetime.date(day=dayS, month=monthS, year=yearS)
        dateR = datetime.date(day=dayR, month=monthR, year=yearR)

#Производим вычисление
        diffDelta = relativedelta(dateS, dateR)

#Результат
        print('Год(а):', diffDelta.years)
        print('Месяцев:', diffDelta.months)
        print('Дней:', diffDelta.days + 1)
        print('=======================================')
        print('Для изменения даты отбора перезапустите программу')
        print('Для выхода наберите exit')