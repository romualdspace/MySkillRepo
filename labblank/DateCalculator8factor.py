import datetime 
from dateutil.relativedelta import relativedelta

dateSelect=input('Дата отбора в формате ДД.ММ.ГГГГ:')
dateRelease=input('Дата изготовления в формате ДД.ММ.ГГГГ:')

dayS, monthS, yearS = map(int, dateSelect.split('.'))
dayR, monthR, yearR = map(int, dateRelease.split('.'))

dateS=datetime.date(day=dayS, month=monthS, year=yearS)
dateR=datetime.date(day=dayR, month=monthR, year=yearR)

diffDelta=relativedelta(dateS, dateR)

print('Лет:', diffDelta.years)
print('Месяцев:', diffDelta.months)
print('Дней:', diffDelta.days+1)