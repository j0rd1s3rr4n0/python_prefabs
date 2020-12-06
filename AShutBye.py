import os
import time
second = 0
minute = 0
hour = 0
start = True
while start != False:	
	second = second + 1
	print("Tiempo de ejecución :",hour,":",minute,":",second)
	os.system('shutdowm /a')
	time.sleep(1)
	os.system('cls')
