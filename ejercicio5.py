entero = [ ]

def mostrarlista():
    for x in range(10):
        numer = int(input('ingesa numeros entero: '))
        entero.append(numer)

def cargarlista():
    print(entero)

mostrarlista()
cargarlista()


