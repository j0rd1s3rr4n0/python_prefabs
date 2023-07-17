import platform
import os
import time
#import pyfiglet

x, y, z = 0, 0, 0  # Define segundos, minutos y horas
s = True           # Define start

sysos = platform.system()
clear = 'cls' if sysos == 'Windows' else 'clear'

def show_time():
    os.system(clear)
    time_str = f"{z:02}:{y:02}:{x:02}"
    #time_ascii = pyfiglet.figlet_format(time_str, font="slant")
    #print(time_ascii) # Imprime con Figlet
    print(time_str) # Imprime normal

while s:
    show_time()
    x = x + 1
    time.sleep(1)
    os.system(clear)
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
        