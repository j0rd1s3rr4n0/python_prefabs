import time
import os
x = 0 #Define segundos
y = 0 #Define minutos
z = 0 #Define horas
s = True #Define start
print('0 : 0 : 0 ~~~~> START')
while s != False:	
	os.system('cls') ## Si se usa en linux usar 'clear'
	x = x + 1
	print('hh:mm:ss')
	print(z,":",y,":",x)
	time.sleep(0)
	if x == 59:
		x = -1
		y = y + 1
	elif y == 60:
		y = 0
		z = z + 1
	elif z == 24:
		x = -1
		y = 0
		z = 0
