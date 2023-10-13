from datetime import datetime
from cliente import Cliente
from renta import Renta
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
                    return fecha
                except ValueError:
                    print("Formato de fecha incorrecto. Utilice el formato YYYY/MM/DD.")    
    
    def fecha_to_str(self, fecha):
        return datetime.strftime(fecha, "%Y/%m/%d")

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
   
    def vehiculo_disponible(self, solo_mostar_disponibles, vehiculo):
        if solo_mostar_disponibles == False:
            return True

        disponible = True
        for renta in self.registro_rentas:
            if vehiculo.identificador in renta.vehiculos:
                if self.fecha_actual >= renta.fecha_inicio and self.fecha_actual <= renta.fecha_fin:
                    disponible = False



        return vehiculo.verificar_disponibilidad(self.fecha_actual) and disponible

    def mostrar_vehiculos(self, solo_mostar_disponibles = False):
        print ("Lista de vehiculos")
        
        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, TransportePasajeros) and self.vehiculo_disponible(solo_mostar_disponibles, vehiculo):
                print("Lista de vehiculos de transporte ")
                print (f"ID: {vehiculo.identificador}")
                print (f"Tipo: {vehiculo.tipo_vehiculo}")
                print (f"Fecha de mantenimiento: {self.fecha_to_str(vehiculo.fecha_mantenimiento)}")
                print(f"Numero de pasajeros: {vehiculo.numero_pasajeros}")
                print("")

        for vehiculo in self.vehiculos:
            if isinstance (vehiculo,TransporteCarga) and self.vehiculo_disponible(solo_mostar_disponibles, vehiculo):
                print("Lista de vehiculos de carga ")
                print (f"ID: {vehiculo.identificador}")
                print (f"Tipo: {vehiculo.tipo_vehiculo}")
                print (f"Fecha de mantenimiento: {self.fecha_to_str(vehiculo.fecha_mantenimiento)}")
                print(f"Capacidad de carga: {vehiculo.capacidad_carga} kg")

    def solicitar_vehiculos(self):
        vehiculos = []
        print("Elije los identificadores de vehiculos a rentar uno por uno")
        self.mostrar_vehiculos(True)
        
        while (opcion := input('Opcion: ')) not in ["r"]:
            print("r) salir")
            vehiculos.append(opcion)

        return vehiculos

    def registar_renta(self):
        #falta pedir vehiculoss
            recoleccion = self.solicitar_fecha("Fecha de recoleccion de vehiculo: ")
            entrega = self.solicitar_fecha("Fecha de entrega del vehiculo: ") 
            #agrega 1 o mas
            nombre = input("Nombre del cliente: ")
            licencia = input("Licencia de manejo: ")
            vehiculos = self.solicitar_vehiculos()

            renta = Renta(recoleccion, entrega, nombre, licencia, vehiculos)
            self.registro_rentas.append(renta)
        
    def mostrar_rentas(self):
        for renta in self.registro_rentas:
            #auto que se rento 
            print("Informacion renta")
            print(f"Nombre del cliente: {renta.nombre_cliente}")
            print(f"Licencia de manejo: {renta.licencia_manejo}")
            print(f"Fecha de recoleccion: {self.fecha_to_str(renta.fecha_inicio)}")
            print(f"Fecha de entrega: {self.fecha_to_str(renta.fecha_fin)}")
            print(f"Vehiculos: {renta.vehiculos}")

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
                    if len(linea) > 1:
                        partes = linea.split(",")
                        print(linea)
                        cliente = Cliente(partes[0],partes[1],partes[2])
                        self.clientes.append(cliente)
                    
        except FileNotFoundError:
             print("No se encontro el archivo clientes.txt") 
        finally:
           file.close()

        try :
            with  open ('vehiculos.txt','r') as  file:
                lineas =file.readlines()
                for linea in lineas:
                    if len(linea) > 1:
                        partes = linea.split(",")
                        print(linea)

                        tipo_transporte = partes[0]
                        identificacion = partes[1]
                        tipo_vehiculo = partes[2]
                        fecha_mantenimiento =  datetime.strptime(partes[3], "%Y/%m/%d")

                        if tipo_transporte == "Pasajeros":
                            numero_pasajeros = int (partes[4])                        
                            vehiculo_personas = TransportePasajeros(identificacion, tipo_vehiculo, fecha_mantenimiento,numero_pasajeros)
                            self.vehiculos.append(vehiculo_personas)
                        elif tipo_transporte == "Carga":
                            capacidad_carga = float (partes[4])
                            vehiculo_carga = TransporteCarga(identificacion, tipo_vehiculo, fecha_mantenimiento,capacidad_carga)
                            self.vehiculos.append(vehiculo_carga)
                        else:
                            print("Entrada no valida")
        
        except FileNotFoundError:
             print("No se encontro el archivo vehiculos.txt")
        finally:
            file.close()

        try :
            with open('rentas.txt','r') as file:
                lineas =file.readlines()
                for linea in lineas:
                    if len(linea) > 1:
                        partes = linea.split(",")
                        print(linea) 
                        fecha_colecta = datetime.strptime(partes[0], "%Y/%m/%d")
                        fecha_entrega = datetime.strptime(partes[1], "%Y/%m/%d")
                        cliente =partes[2]
                        licencia =partes[3]
                        vehiculos =partes[4].split("&")
                        renta = Renta(fecha_colecta,fecha_entrega, cliente, licencia, vehiculos)
                        self.registro_rentas.append(renta)
            
        except FileNotFoundError:
                print("No se encontro el archivo rentas.txt")
        finally:
           file.close()

    def guardar_datos(self):
        try :
            with open('clientes.txt','w') as file:
                lineas = []
                for cliente in self.clientes:
                    lineas.append(cliente.guardar_datos())
                file.writelines(lineas)
        except FileNotFoundError:
            print("NO GUARDO")
        finally:
           file.close()

        try :
            with open('vehiculos.txt','w') as file:
                lineas = []
                for vehiculo in self.vehiculos:
                    lineas.append(vehiculo.guardar_datos())
                print(lineas)
                file.writelines(lineas)
        except FileNotFoundError:
            print("NO SE PUDO GR")
        finally:
           file.close()

        try :
            with open('rentas.txt','w') as file:
                lineas = []
                for renta in self.registro_rentas:
                    lineas.append(renta.guardar_datos())
                file.writelines(lineas)
        except FileNotFoundError:
            print("NO SE PUDO GUARDAR")
        finally:
           file.close()

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