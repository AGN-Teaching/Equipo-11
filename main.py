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
            fecha = datetime.strptime(fecha_str, "%Y/%m/%d")
            return fecha.strftime("%Y/%m/%d")
        except ValueError:
            print("Formato de fecha incorrecto. Utilice el formato YYYY/MM/DD.")

# Función para verificar que la fecha de recolección sea anterior a la fecha de entrega
def verificar_fechas(fecha_recoleccion, fecha_entrega):
    try:
        fecha_recoleccion = datetime.strptime(fecha_recoleccion, "%Y/%m/%d")
        fecha_entrega = datetime.strptime(fecha_entrega, "%Y/%m/%d")
        if fecha_recoleccion < fecha_entrega:
            return True
        else:
            return False
    except ValueError:
        return False

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
def solicitar_disponibilidad():
    while True:
        disponibilidad = input("¿El vehículo está disponible? (sí/no): ").lower()
        if disponibilidad in ("sí", "no"):
            return disponibilidad == "sí"
        else:
            print("Respuesta no válida. Responda 'sí' o 'no'.")

# Función para solicitar el número de tarjeta de crédito con exactamente 16 dígitos
def solicitar_numero_tarjeta():
    while True:
        numero_tarjeta = input("Número de tarjeta de crédito (16 dígitos): ")
        if len(numero_tarjeta) == 16 and numero_tarjeta.isdigit():
            return numero_tarjeta
        else:
            print("El número de tarjeta de crédito debe contener exactamente 16 dígitos.")

# Función para solicitar una identificación válida del conductor (8 dígitos y una letra)
def solicitar_identificacion_conductor():
    while True:
        identificacion = input("Identificación del conductor (8 dígitos y una letra): ")
        if len(identificacion) == 9 and identificacion[:8].isdigit() and identificacion[8].isalpha():
            return identificacion
        else:
            print("La identificación del conductor debe contener 8 dígitos seguidos de una letra.")

# Restringir la fecha de recolección para ser igual o posterior a la fecha actual
fecha_actual = datetime.now().strftime("%Y/%m/%d")
fecha_recoleccion = solicitar_fecha(f"Fecha de recolección del transporte (a partir de {fecha_actual}): ")
while fecha_recoleccion < fecha_actual:
    print("La fecha de recolección debe ser igual o posterior a la fecha actual.")
    fecha_recoleccion = solicitar_fecha(f"Fecha de recolección del transporte (a partir de {fecha_actual}): ")

# Solicitar los datos del cliente
cliente = Cliente(input("Nombre del cliente: "), input("Identificación del cliente: "), TarjetaCredito(solicitar_numero_tarjeta(), input("Fecha de vencimiento de la tarjeta de crédito (YYYY/MM): ")))

# Solicitar los datos del vehículo de pasajeros
tipo_vehiculo_pasajeros = solicitar_tipo_vehiculo()
if tipo_vehiculo_pasajeros == "pasajeros":
    vehiculo_pasajeros = VehiculoPasajeros(int(input("Capacidad de pasajeros del vehículo: ")), input("Modelo del vehículo: "))
else:
    vehiculo_pasajeros = VehiculoCarga(int(input("Capacidad de carga del vehículo (en kg): ")), int(input("Carga máxima del vehículo (en kg): ")))
disponibilidad_pasajeros = solicitar_disponibilidad()
vehiculo_pasajeros.disponible = disponibilidad_pasajeros

# Solicitar los datos del vehículo de carga
tipo_vehiculo_carga = solicitar_tipo_vehiculo()
if tipo_vehiculo_carga == "pasajeros":
    vehiculo_carga = VehiculoPasajeros(int(input("Capacidad de pasajeros del vehículo: ")), input("Modelo del vehículo: "))
else:
    vehiculo_carga = VehiculoCarga(int(input("Capacidad de carga del vehículo (en kg): ")), int(input("Carga máxima del vehículo (en kg): ")))
disponibilidad_carga = solicitar_disponibilidad()
vehiculo_carga.disponible = disponibilidad_carga

# Solicitar los datos del transporte
fecha_recoleccion = solicitar_fecha("Fecha de recolección del transporte (YYYY/MM/DD): ")
fecha_entrega = solicitar_fecha("Fecha de entrega del transporte (YYYY/MM/DD): ")

while not verificar_fechas(fecha_recoleccion, fecha_entrega):
    print("La fecha de recolección debe ser anterior a la fecha de entrega.")
    fecha_recoleccion = solicitar_fecha("Fecha de recolección del transporte (YYYY/MM/DD): ")
    fecha_entrega = solicitar_fecha("Fecha de entrega del transporte (YYYY/MM/DD): ")

# Solicitar los datos del conductor
conductor = Persona(input("Nombre de la persona: "), solicitar_identificacion_conductor())

# Agregar los vehículos al transporte
transporte_pasajeros = Transporte(fecha_recoleccion, fecha_entrega)
transporte_pasajeros.agregar_vehiculo(vehiculo_pasajeros)
transporte_pasajeros.agregar_vehiculo(vehiculo_carga)

# Agregar el conductor al transporte
transporte_pasajeros.agregar_conductor(conductor)

# Asociar el transporte al cliente
cliente.rentar_transporte(transporte_pasajeros)

# Mostrar la información del cliente y su renta
cliente.mostrar_info()

# Abre el archivo "registro.txt" en modo de escritura y crea el archivo si no existe
with open("registro.txt", "w") as archivo_registro:
    archivo_registro.write("Registro de Datos:\n")
    archivo_registro.write(f"Nombre del cliente: {cliente.nombre}\n")
    archivo_registro.write(f"Identificación del cliente: {cliente.identificacion}\n")
    archivo_registro.write(f"Número de tarjeta de crédito: {cliente.tarjeta_credito.numero}\n")
    archivo_registro.write(f"Fecha de vencimiento de la tarjeta: {cliente.tarjeta_credito.fecha_vencimiento.strftime('%Y/%m')}\n")
    archivo_registro.write(f"Fecha de recolección del transporte: {transporte_pasajeros.fecha_recoleccion}\n")
    archivo_registro.write(f"Fecha de entrega del transporte: {transporte_pasajeros.fecha_entrega}\n")
    archivo_registro.write(f"Nombre del conductor: {conductor.nombre}\n")
    archivo_registro.write(f"Identificación del conductor: {conductor.identificacion}\n")

print("Datos registrados con éxito en el archivo 'registro.txt'.")


