import time
import pywhatkit as kit

import datetime

phone = str(input("Number: +34"))
num = "+34"+str(phone)
msg = str(input("Message: "))

now = datetime.datetime.now()
hour = now.hour
minute = int(now.minute)+1

kit.sendwhatmsg(num,msg,hour,minute)
mumu = "Enviado "+str(msg)+" a "+str(num)+" aproximadamente a "+str(hour)+":"+str(minute)
print(mumu)
time.sleep(5)
