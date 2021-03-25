print('4.Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.\n')

nombre1 = ['ramon','pedro', 'manuel' , 'jesus']
nombre2 = ['moises', 'manolo' , 'pedrito', 'ramona']

def superposicion ():
    contador = 0
    for x in nombre1:
        for i in nombre2:
            if x == i:
                contador+=1

    if contador > 0:
        print(True)
    else:
        print(False)

superposicion()