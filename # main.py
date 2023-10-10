# main.py

from datetime import datetime
from tarjeta_credito import TarjetaCredito
from vehiculo import VehiculoPasajeros, VehiculoCarga
from transporte import Transporte
from cliente import Cliente
from persona import Persona

# Función para solicitar una fecha válida
def solicitar_fecha(prompt):
    while True:
        fecha_str = input(prompt)
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            return fecha.strftime("%Y-%m-%d")
        except ValueError:
            print("Formato de fecha incorrecto. Utilice el formato YYYY-MM-DD.")

# Función para solicitar una carga válida
def solicitar_carga(prompt):
    while True:
        carga_str = input(prompt)
        try:
            carga = int(carga_str)
            if carga < 0:
                print("La carga no puede ser negativa.")
            else:
                return carga
        except ValueError:
            print("Debe ingresar un número entero válido para la carga.")

# Función para solicitar si el vehículo es de pasajeros o de carga
def solicitar_tipo_vehiculo():
    while True:
        tipo = input("Tipo de vehículo (pasajeros/carga): ").lower()
        if tipo in ("pasajeros", "carga"):
            return tipo
        else:
            print("Tipo de vehículo no válido. Ingrese 'pasajeros' o 'carga'.")

# Función para solicitar si el vehículo está disponible