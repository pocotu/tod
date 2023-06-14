'''
Haciendo uso de las palabras reservadas “try”, “except” y de la definición de “función
dentro de otra función” desarrolle una función que describa las siguientes acciones:
Soy "funcionPrincipal" intentando llamar a "funcionSegundaria" antes de ser creada,
no se puede.
Hola soy "funcionPrincipal" llamando a "funcionSegundaria" de nuevo.
Hola soy "funcionSegundaria".
'''

def funcionPrincipal():
    try:
        print('Soy "funcionPrincipal" intentando llamar a "funcionSegundaria" antes de ser creada, no se puede.')
        funcionSegundaria()
    except:
        print('Hola soy "funcionPrincipal" llamando a "funcionSegundaria" de nuevo.')
        def funcionSegundaria():
            print('Hola soy "funcionSegundaria".')
        funcionSegundaria()

funcionPrincipal()

