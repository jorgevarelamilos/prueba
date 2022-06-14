datos=""
with open('p10k12w01.txt') as fname:
    lineas=fname.readlines()
    for linea in lineas:
        #datos.append(linea.strip('\n'))
        datos=datos+linea
    print(datos)