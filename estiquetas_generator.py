idiomas_list = ['es','en','ca','fr','it','de']
while True:
    etiqueta = input("Ingrese la etiqueta: ").replace("trad.", "").replace("etiquetes.", "")
    if etiqueta == "!!":
        break

    contenido = input("Ingrese el contenido: ")
    idioma = ''
    while idioma not in idiomas_list:
        idioma = input("Ingrese el idioma: ")

    linea_sql = f"INSERT INTO `caraalvent`.`web_t_etiquetes` (`id_pagina`, `nomEtiqueta`, `contingut`, `idioma`) VALUES ('0', '{etiqueta}', '{contenido}', '{idioma}');"

    with open("nuevas_etiquetas.sql", "a") as archivo_sql:
        archivo_sql.write(linea_sql + "\n")

print("Se ha terminado de ingresar etiquetas. El bucle ha finalizado.")
