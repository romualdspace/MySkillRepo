#Импортируем библиотеки
import random

#На входе берем количество необходимых исследований
i=int(input("Введите количество анализов:"))

#Открываем файл для записи
f=open("Генератор анализов.txt", "at" )

#Запускаем цикл
while i>0:
    volume = random.randint(50, 200) #объем мочи
    # определяем цвет мочи. Чаще всего должна быть "жёлтой", чуть реже "светло-желтой", более редкой "тёмно-жёлтой"
    colorint=random.randint(0,100)
    if colorint > 80:
        color=('тёмно-желтая')
    elif 40<colorint<80:
        color=('жёлтая')
    else:
        color=('светло-жёлтая')
    reaction = random.randint(5, 8) #pH мочи
    relweight = random.randint(1005, 1025) #удельный вес мочи
    wbc = ["0-1", "1-2", "2-3", "един."] # клетки
    random.shuffle(wbc)
    finwbc = wbc.pop()
    rbc = ["0-1", "1-2", "един."]
    random.shuffle(rbc)
    finrbc = rbc.pop()
    epit = ["0-1", "1-2", "2-3", "3-5", "един."]
    finepit = epit.pop()
    random.shuffle(epit)
    #Вывод в консоль
    print ("Доставленное количество:", volume)
    print ("Цвет:", color)
    print ("Прозрачность: прозрачная")
    print ("Осадок:     нет")
    print ("Реакция:   ", reaction)
    print ("Удельный вес:", relweight)
    print ("Белок:      отриц.")
    print ("Сахар:      отриц.")
    print ("Уробилин:   отриц.")
    print ("Желч.пигм.: отриц.")
    print ("Лейкоциты: ", finwbc)
    print ("Эритроциты:", finrbc)
    print ("Цилиндры:   отриц.")
    print ("Эпителий:  ", finepit)
    print ("Слизь:      отриц.")
    print ("Соли:       отриц.")
    print ("=======================")
   #Запись в файл
    #f=open("Генератор анализов.txt", "at" )
    f.write("Дост. кол-во:  %s" %(volume))
    f.write("\n")
    f.write("Цвет:       %s" %(color))
    f.write("\n")
    f.write("Осадок:     нет")
    f.write("\n")
    f.write("Реакция:    %s" %(reaction))
    f.write("\n")
    f.write("Удельный вес:%s" %(relweight))
    f.write("\n")
    f.write("Белок:      отриц.")
    f.write("\n")
    f.write("Сахар:      отриц.")
    f.write("\n")
    f.write("Уробилин:   отриц.")
    f.write("\n")
    f.write("Желч.пигм.: отриц.")
    f.write("\n")
    f.write("Лейкоциты:  %s" %(finwbc))
    f.write("\n")
    f.write("Эритроциты: %s" %(finrbc))
    f.write("\n")
    f.write("Цилиндры:   отриц.")
    f.write("\n")
    f.write("Эпителий:   %s" %(finepit))
    f.write("\n")
    f.write ("Слизь:      отриц.")
    f.write("\n")
    f.write ("Соли:       отриц.")
    f.write("\n")
    f.write ("=======================")
    f.write("\n")
    #f.close()
    i-=1
f.close()    
input("Press Enter to quit")