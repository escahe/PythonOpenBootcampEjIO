from escribir import escribirTXT
pares = ['Pares:']
impares = ['Impares:']
# generamos listas de números pares e impares entre 0 y 20
for i in range(0, 21):
    if i % 2:
        impares.append(i)
    else:
        pares.append(i)
# escribimos la lista de pares en app.txt:
escribirTXT(pares)
#escribimos la lista de impares en app.txt:
escribirTXT(impares)