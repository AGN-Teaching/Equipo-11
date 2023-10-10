# persona.py

class Persona:
    def _init_(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Identificación: {self.identificacion}")