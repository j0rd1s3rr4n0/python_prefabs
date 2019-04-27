import os
import time
second = 0
minute = 0
hour = 0
start = True
while start != False:	
	second = second + 1
	print(hour,":",minute,":",second)
	time.sleep(1)
	if second == 0.5:
		os.system('shutdowm -a')
		os.system('cls')
