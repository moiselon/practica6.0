class contacto1():
    nombre = ' '
    apellido = ' '
    telefono = ' '
    direccion = ' '

conta1 = contacto1()

conta1.nombre = input(' ingresa su nombre: ')
conta1.apellido = input(' ingresa su apellido: ')
conta1.telefono = input(' ingresa su telefono: ')
conta1.direccion = input(' ingresa su direccion: ')

class contacto2():
    nombre1 = ' '
    telefono1 = '809-548-0045 '
    direccion1 = ' '
    apellido1= ' '

print('_______________________________')
print('llamando a contacto2...........')
print('________________________________\n')

conta2 = contacto2()
conta2.nombre1 = input(' ingresa su nombre: ')
conta2.apellido1 = input(' ingresa el apellido: ')
conta2.direccion1 = input(' ingresa su direccion: ')
print(' hola mi nombres es ', conta1.nombre , 'mi apellido es' , conta1.apellido, 'mi direccion es' , conta1.direccion, 'mi telefono es', conta1.telefono , '\n')
print(' hola mi nombres es ' 'mi apellido es' , conta2.apellido1, conta2.nombre1 , 'mi direccion es'  , conta2.direccion1, 'mi telefono es', conta2.telefono1 )