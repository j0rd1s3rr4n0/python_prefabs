import os
import time
from win10toast import ToastNotifier
import getpass
username = "User: "+str(getpass.getuser())
def notification():
	os.chdir(os.path.dirname(os.path.realpath( __file__)))
	toast = ToastNotifier()
	title = "Notification"
	message = str(time.asctime()+"\n"+username+"\n"+awd)
	icon = "icon.ico"
	length = 10
	toast.show_toast(title,message,icon_path=icon, duration=length)

notification()
