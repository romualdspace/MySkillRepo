while True:
	volume = int(input('Объем: '))
	hbcommon = int(input('HB общий: '))
	const100 = 100
	volcorrect = (volume + const100)/1000
	hbdose = hbcommon*volcorrect
	print('%0.0f' % (hbdose))
