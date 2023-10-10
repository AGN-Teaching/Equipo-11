# vehiculo.py

from abc import ABC, abstractmethod

# Clase abstracta para representar vehículos
class Vehiculo(ABC):
    def _init_(self, capacidad):
        self.capacidad = capacidad
        self.disponible = True

    @abstractmethod
    def mostrar_info(self):
        pass

    def marcar_mantenimiento(self):
        self.disponible = False

    def desmarcar_mantenimiento(self):
        self.disponible = True

# Clases concretas para tipos de vehículos
class VehiculoPasajeros(Vehiculo):
    def _init_(self, capacidad, modelo):
        super()._init_(capacidad)
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Tipo: Pasajeros")
        print(f"Capacidad de Pasajeros: {self.capacidad}")
        print(f"Modelo: {self.modelo}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")

class VehiculoCarga(Vehiculo):
    def _init_(self, capacidad, carga_maxima):
        super()._init_(capacidad)
        self.carga_maxima = carga_maxima

    def mostrar_info(self):
        print(f"Tipo: Carga")
        print(f"Capacidad de Carga: {self.capacidad} kg")
        print(f"Carga Máxima: {self.carga_maxima} kg")
        print(f"Disponible: {'Sí' if self.disponible else'No'}")