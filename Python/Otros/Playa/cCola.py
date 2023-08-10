# Esta clase implementa una cola de elementos de cualquier tipo
# con la particularidad de que el primer elemento en entrar es el 
# primero en salir
# Tiene la siguiente estructura:
# elemento -> subCola -> elemento -> subCola -> elemento -> subCola -> None
# donde None indica que la cola esta vacia
# El diagrama de clases es el siguiente:
# CCola
#   - elemento
#   - subCola
#   + es_vacia()
#   + agregar(elemento)
#   + avanzar()
#   + primero()

class CCola:
    # Constructor
    # Inicializa la cola como vacia
    # __init__ es el constructor de la clase CCola
    # toda clase tiene un constructor que se llama __init__ 
    # y que se ejecuta cuando se crea un objeto de esa clase
    # self es el puntero al objeto que se esta creando

    def __init__(self): 
        self.elemento = None
        self.subCola = None
    
    # Metodos
    # es_vacia() -> bool
    # Devuelve True si la cola esta vacia, False en caso contrario
    def es_vacia(self):
        return self.elemento is None

    def agregar(self, elemento):
        if self.es_vacia():
            self.elemento = elemento
            self.subCola = CCola()
        else:
            self.subCola.agregar(elemento)

    def avanzar(self):
        if not self.es_vacia():
            self.elemento = self.subCola.elemento
            self.subCola = self.subCola.subCola

    def primero(self):
        return self.elemento

# El diagrama de flujo es el siguiente:
# Inicio
#   Crear cola
#   Mientras cola no este vacia
#       Mostrar primero de la cola
#       Avanzar cola
#   Fin mientras
# Fin
