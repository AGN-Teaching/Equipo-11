from datetime import datetime
from cliente import Cliente
from registrorentas import RegistroRenta
from transporte import Transporte, TransporteCarga, TransportePasajeros
from menu import Menu

class SistemaDeTransporte:
    def __init__(self):
        self.vehiculos = []
        self.clientes = []
        self.registro_rentas = []
        self.fecha_actual = datetime.now()

    @staticmethod
    def solicitar_fecha(prompt):
            while True:
                fecha_str = input(prompt)
                try:
                    fecha = datetime.strptime(fecha_str, "%Y/%m/%d")
                    return fecha.strftime("%Y/%m/%d")
                except ValueError:
                    print("Formato de fecha incorrecto. Utilice el formato YYYY/MM/DD.")    
    
    def registro_cliente(self):
        nombre = input("Nombre del cliente: ")
        identificacion = input("Identificacion del cliente: ")
        tarjeta = input("Numero de tarjeta de credito: ") #Restriccion de digitos
        cliente = Cliente (nombre, identificacion , tarjeta)
        self.clientes.append(cliente)

    def mostrar_clientes(self):
        print ("Registro de clientes")
        print ("")   
        for cliente in self.clientes:
            print(f"Nombre cliente: {cliente.nombre}")
            print(f"Identificacion cliente: {cliente.identificacion}")
            print(f"Tarjeta cliente: {cliente.tarjeta_credito}")
            print("")
   
    def mostrar_vehiculos(self):
        print ("Lista de vehiculos")
        
        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, TransportePasajeros):
                print("Lista de vehiculos de transporte ")
                print (f"ID: {vehiculo.identificador}")
                print (f"Tipo: {vehiculo.tipo_vehiculo}")
                print (f"Fecha de mantenimiento: {vehiculo.fecha_mantenimiento}")
                print(f"Numero de pasajeros: {vehiculo.numero_pasajeros}")
                print("")

        for vehiculo in self.vehiculos:
            if isinstance (vehiculo,TransporteCarga):
                print("Lista de vehiculos de carga ")
                print (f"ID: {vehiculo.identificador}")
                print (f"Tipo: {vehiculo.tipo_vehiculo}")
                print (f"Fecha de mantenimiento: {vehiculo.fecha_mantenimiento}")
                print(f"Capacidad de carga: {vehiculo.capacidad_carga} kg")

    def registar_renta(self):
        #falta pedir vehiculoss
            recoleccion = self.solicitar_fecha("Fecha de recoleccion de vehiculo: ")
            entrega = self.solicitar_fecha("Fecha de entrega del vehiculo: ") 
            #agrega 1 o mas
            nombre = input("Nombre del cliente: ")
            licencia = input("Licencia de manejo: ")
            renta = RegistroRenta(recoleccion, entrega,nombre, licencia)
            self.registro_rentas.append(renta)
        
    def mostrar_rentas(self):
        for renta in self.registro_rentas:
            #auto que se rento 
            print("Informacion renta")
            print(f"Nombre del cliente: {renta.nombre_cliente}")
            print(f"Licencia de manejo: {renta.licencia_manejo}")
            print(f"Fecha de recoleccion: {renta.fecha_inicio}")
            print(f"Fecha de entrega: {renta.fecha_fin}")

    def registrar_vehiculo(self):
        id = input("Registre identificador de vehiculo: ")
        tipo = input ("Registre tipo de vehiculo: ")
        fecha = self.solicitar_fecha("Registre fecha de mantenimiento:  ")
        transporte = input ("¿El transporte es de pasajeros o de carga (p/c)?: ")   

        if transporte == "p":
            personas = input("Registre el numero de personas: ")
            vehiculo_personas = TransportePasajeros(id,tipo,fecha,personas)
            self.vehiculos.append(vehiculo_personas)
        elif transporte == "c":
            carga = input("Registre capacidad de carga en kilogramos: ")
            vehiculo_carga = TransporteCarga(id,tipo,fecha,carga)
            self.vehiculos.append(vehiculo_carga)
        else :
            print("Seleccion no valida")

    def cargar_datos(self):
        try : 
            with open('clientes.txt','r') as file:
                lineas =file.readlines()
                for linea in lineas:
                    partes = linea.split(",")
                    #print(linea)
                    cliente = Cliente(partes[0],partes[1],partes[2])
                    self.clientes.append(cliente)
                    
        except FileNotFoundError:
             print("No se encontro el archivo clientes.txt") 
        
        try :
            with  open ('vehiculos.txt','r') as  file:
                lineas =file.readlines()
                for linea in lineas:
                    partes = linea.split(",")
                    print(linea)

                    tipo_vehiculo = partes[0]
                    identificacion = int(partes[1])
                    #fechaM =fecha(partes[3])
                    if tipo_vehiculo == "Pasajeros":
                        numero_pasajeros = int (partes[4])                        
                        vehiculo_personas = TransportePasajeros(identificacion,partes[2],partes[3],numero_pasajeros)
                        self.vehiculos.append(vehiculo_personas)
                    elif tipo_vehiculo == "Carga":
                        capacidad_carga = float (partes[4])
                        vehiculo_carga = TransporteCarga(identificacion,partes[2],partes[3],capacidad_carga)
                        self.vehiculos.append(vehiculo_carga)
                    else:
                        print("Entrada no valida")
        
        except FileNotFoundError:
             print("No se encontro el archivo vehiculos.txt")

        try :
            with open('rentas.txt','r') as file:
                lineas =file.readlines()
                for linea in lineas:
                    partes = linea.split(",")
                    print(linea) 
                    renta = RegistroRenta(partes[0],partes[1],partes[2],partes[3])#falta pedir vehiculo[4]
                    self.registro_rentas.append(renta)
            
        except FileNotFoundError:
                print("No se encontro el archivo rentas.txt")

    
    def guardar_datos(self,datos, lista_datos):
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

    def menu(self):
        print("Menu")
        menu = Menu()
        opciones = {
            '1': ('Registrar cliente', self.registro_cliente),
            '2': ('Mostrar clientes', self.mostrar_clientes),
            '3': ('Mostar lista de Vehiculos', self.mostrar_vehiculos),
            '4': ('Registar una renta', self.registar_renta),
            '5': ('Mostrar rentas', self.mostrar_rentas),
            '6': ('Registar vehiculo', self.registrar_vehiculo),
            '7': ('Guardar datos', self.guardar_datos),
            '8': ('Cargar datos',self.cargar_datos),
            '9': ('Salir',exit),
        }

        menu.generar_menu(opciones, '9')