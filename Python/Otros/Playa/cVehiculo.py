# Crear una clase que tenga de atributo solo el tipo de vehiculo (auto, moto, camioneta, etc)

class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"Tipo de vehiculo: {self.tipo}"


