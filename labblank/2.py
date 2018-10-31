import random
i=int(input("Введите количество анализов:"))
while i>0:
    volume = random.randint(50, 200)
    color = ["светло-жёлтая", "желтая","желтая","желтая","желтая","желтая","желтая","желтая","желтая","светло-жёлтая","светло-жёлтая","светло-жёлтая","светло-жёлтая","светло-жёлтая", "тёмно-желтая"]
    random.shuffle(color)
    reaction = random.randint(5, 8)
    relweight = random.randint(1005, 1025)
    wbc = ["0-1", "1-2", "2-3", "един."]
    random.shuffle(wbc)
    rbc = ["0-1", "1-2", "един."]
    random.shuffle(rbc)
    epit = ["0-1", "1-2", "2-3", "3-5", "един."]
    random.shuffle(epit)
    print ("Доставленное количество:", volume)
    print ("Цвет:", color.pop())
    print ("Прозрачность: прозрачная")
    print ("Осадок: нет")
    print ("Реакция:", reaction)
    print ("Удельный вес:", relweight)
    print ("Белок:     отриц.")
    print ("Сахар:     отриц.")
    print ("Уробилин:  отриц.")
    print ("Желч.пигм.:отриц.")
    print ("Лейкоциты: ", wbc.pop())
    print ("Эритроциты:", rbc.pop())
    print ("Цилиндры:   отриц.")
    print ("Эпителий:  ", epit.pop())
    print ("Слизь:     отриц.")
    print ("Соли:      отриц.")
    print ("=======================")
    i=i-1
input("Press Enter to quit")
