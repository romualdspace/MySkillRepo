#Таблица значений влажного термометра
wetlist = [i/10 for i in range(150,255,5)]

modwetlist1half = [i/100 for i in range(0,11,1)]
modwetlist1half.reverse()

modwetlist2half = [i/100 for i in range(2,21,2)]
mod = modwetlist1half + modwetlist2half

wetList = dict(zip(wetlist, mod))

print(wetList)