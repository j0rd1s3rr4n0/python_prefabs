import os
import time
if opsi == "windows" or "linux":
	second = 0
	minute = 0
	hour = 0
	start = True
while start != False:	
	second = second + 1
	print(hour,":",minute,":",second)
	time.sleep(1)
	if second == 5:
		"""os.system('shutdowm -a')
		os.system('cls')"""	
		#If you use windows
		"""os.system('shutdowm -a')
		os.system('cls')"""
