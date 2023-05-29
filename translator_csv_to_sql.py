# -*- coding: utf-8 -*-
import csv
import sys
from tkinter import *
from tkinter import filedialog
from translate import Translator
from tkinter import messagebox
import webbrowser
import ctypes

idiomas_list = ['es','en','ca','fr','it','de']
idioma_origen = ''
idioma_destino = ''
tabla_name = ''
# Configurar el proxy
proxy = {
'http':'http://37.235.24.194:3128',
'https':'https://37.235.24.194:3128',
}
proxy_switch = False

# Función para traducir un texto utilizando la biblioteca translate y un proxy
def traducir(texto, idioma_origen, idioma_destino,proxy_switch):
    translator = Translator(from_lang=idioma_origen, to_lang=idioma_destino)
    if proxy_switch:
        traduccion = translator.translate(texto) # Implement Proxy to bypass Free Trial Limit
    else:
        traduccion = translator.translate(texto)
    return traduccion

# Función para realizar la tarea de traducción y generación del archivo SQL
def realizar_tarea():
    # Obtener el contenido del campo de entrada
    nombre = entrada_nombre.get()

    if not nombre:
        # Mostrar un mensaje de error si el campo está vacío
        messagebox.showerror('Error', 'Nombre Del Nuevo Archivo SQL Requerido')
        return

    # Obtener la ruta del archivo CSV
    ruta_csv = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if ruta_csv:
        # Obtener el nombre del archivo
        nombre_archivo = ruta_csv.split('/')[-1].split('.')[0]

        # Abrir el archivo CSV y leer su contenido
        with open(ruta_csv, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=';')
            lineas = list(lector_csv)
            ventana.title('Tarea de traducción y generación de archivo SQL [Traduciendo]')
            # Recorrer las líneas del CSV, empezando desde la segunda línea
            for linea in lineas[1:]:
                # Obtener el texto en la posición 3
                texto = linea[3]

                # Traducir el texto del idioma_origen a idioma_destino
                texto_traducido = traducir(texto, idioma_origen, idioma_destino,proxy_switch)
                texto_traducido = texto_traducido.replace("'","''")

                # Reemplazar el texto original con el texto traducido en la posición 3
                linea[3] = texto_traducido

        # Generar el nombre del archivo SQL
        nombre_sql = entrada_nombre + '.sql'
        ventana.title('Tarea de traducción y generación de archivo SQL [Reemplazando Contenido]')
        # Guardar los cambios en el archivo CSV
        with open(ruta_csv, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv, delimiter=';')
            escritor_csv.writerows(lineas)
        ventana.title('Tarea de traducción y generación de archivo SQL [Generando Archivo SQL]')
        # Generar el archivo SQL con los datos modificados
        with open(nombre_sql, 'w') as archivo_sql:
            archivo_sql.write('INSERT INTO '+tabla_name+' (id_pagina, nomEtiqueta, contingut, idioma) VALUES\n')
            for linea in lineas[1:]:
                id_pagina = linea[1]
                nom_etiqueta = linea[2]
                contingut = linea[3]
                idioma = linea[4]
                archivo_sql.write(f"({id_pagina}, '{nom_etiqueta}', '{contingut}', '{idioma}'),\n")

        # Mostrar un mensaje de finalización
        messagebox.showinfo('Tarea completada', f"La tarea ha sido completada. Se ha generado el archivo {nombre_sql}")
        ventana.title('Tarea de traducción y generación de archivo SQL [COMPLETADO]')

# Función para solicitar ejecución como administrador
def solicitar_administrador():
    # Comprobar si el programa se está ejecutando como administrador
    if ctypes.windll.shell32.IsUserAnAdmin():
        # Si ya se está ejecutando como administrador, iniciar la tarea directamente
        realizar_tarea()
    else:
        # Si no se está ejecutando como administrador, volver a ejecutar el programa solicitando privilegios de administrador
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        exit()

# Función para configurar el texto del botón
def configurar_texto_boton():
    if ctypes.windll.shell32.IsUserAnAdmin():
        boton_iniciar.config(text='Iniciar tarea', command=realizar_tarea)
    else:
        boton_iniciar.config(text='Ejecutar como administrador', command=solicitar_administrador)
# Función para abrir el enlace en el navegador
def abrir_enlace(event):
    webbrowser.open("https://github.com/j0rd1s3rr4n0")

print("Idiomas Disponibles:")
for idioma in idiomas_list:
    print(" - "+idioma)
while idioma_origen not in idiomas_list:
    idioma_origen = input("Idioma Original: ")

while idioma_destino not in idiomas_list:
    idioma_destino = input("Idioma Final: ")
tabla_name = ''
while len(tabla_name) < 3:
    tabla_name = str(input("Nombre de la tabla de Base de Datos: "))
switch_txt_proxy = ''
while switch_txt_proxy.upper() not in ['SI','SÍ','NO','S','N']:
    switch_txt_proxy = str(input("Usar Proxy (S/N): "))
if(switch_txt_proxy in ['SI','S','SÍ']):
    proxy_switch = True

# Crear la ventana principal
ventana = Tk()

# Configurar la ventana
ventana.title('Tarea de traducción y generación de archivo SQL')
ventana.geometry('550x100')

# Crear un label descriptivo
label_nombre = Label(ventana, text='Nombre del nuevo archivo SQL:')
label_nombre.pack()

# Crear un campo de entrada
entrada_nombre = Entry(ventana)
entrada_nombre.pack(pady=5)

# Crear un botón para iniciar la tarea
boton_iniciar = Button(ventana, text='', command=solicitar_administrador)
boton_iniciar.pack()

# Configurar el texto del botón al cargar la ventana
configurar_texto_boton()

# Crear un label enlace
label_enlace = Label(ventana, text='Developed By J0rd1S3rr4n0', fg='blue', cursor='hand2')
label_enlace.pack()
label_enlace.bind('<Button-1>', abrir_enlace)

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()
