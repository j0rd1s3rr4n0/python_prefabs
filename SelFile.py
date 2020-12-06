from tkinter import Tk
from tkinter.filedialog import askopenfilename
def Abrir():
	Tk().withdraw()
	#filename = askopenfilename() 
	filename = askopenfilename(title="Hello",filetypes=[
		("Text files","*.txt"),          # Encrypt with 
		("Encripted files","*.jk"),      # Encrypt with 
		("Executable files","*.exe"),    # Encrypt with 
		("Dash files","*.___"),          # Encrypt with 
		("F Society files","*.fsty"),    # Encrypt with 
		("Brokeware files","*.bkw"),     # Encrypt with 
		("Parthenoun files","*.pth"),])  # Encrypt with 
	#filename = askopenfilename(parent=Tk(),filetypes=[("Text files","*.txt")]) 
Abrir()
