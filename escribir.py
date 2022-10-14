def escribirTXT(contenido:list):
    """
    Recibe como parámetro una lista con las líneas y las escribe
    en app.txt. Cada item de la lista es una línea, no necesita contener "\\n"
    """
    with open('app.txt','a') as archivo:
        for linea in contenido:
            archivo.write(str(linea)+'\n')