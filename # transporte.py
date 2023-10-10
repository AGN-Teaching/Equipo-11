# transporte.py

from vehiculo import Vehiculo
from persona import Persona

class Transporte:
    def _init_(self, fecha_recoleccion, fecha_entrega):
        self.fecha_recoleccion = fecha_recoleccion
        self.fecha_entrega = fecha_entrega
        self.vehiculos = []
        self.conductores = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def agregar_conductor(self, conductor):
        self.conductores.append(conductor)

    def mostrar_info(self):
        print(f"Fecha de Recolección: {self.fecha_recoleccion}")
        print(f"Fecha de Entrega: {self.fecha_entrega}")
        print("Vehículos:")
        for vehiculo in self.vehiculos:
            vehiculo.mostrar_info()
        print("Conductores:")
        for conductor in self.conductores:
            conductor.mostrar_info()