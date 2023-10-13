[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/XixB-tii)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12235114)

![UAM](https://github.com/AGN-Teaching/Equipo-11/assets/125590988/a78397fe-a510-47b4-bd1d-6ee4561f44e8)

# PROYECTO FINAL
UNIVERSIDAD AUTÓNOMA METROPOLITANA  "UNIDAD   CUAJIMALPA"
# RENTA DE TRANSPORTE
LICENCIATURA: INGENIERÍA EN COMPUTACIÓN 


UEA: *PROGRAMACIÓN ORIENTADA A OBJETOS*



*ESTUDIANTE:*


- NAVA MARTINEZ DANIELA                 2223028762
- OLGUIN RICO ANAID                     2203024973
- RAMIREZ AGUILERA JESUS EMMANUEL       2223068873

*PROFESOR:* 


Abel García Nájera


# RESUMEN
<p align="justify">
El proyecto final del curso "Programación Orientada a Objetos" se concentra en la aplicación de los conceptos aprendidos a lo largo del trimestre. Esto incluye el uso de conceptos como polimorfismo, herencia, clases, subclases, entre otros. Además, destacamos la relevancia de los diagramas UML para organizar y visualizar las clases, sus atributos y los métodos que contienen.
</p>

<p align="justify">
El propósito principal de este proyecto es desarrollar un servicio de transporte que ofrece dos modalidades: transporte de pasajeros y transporte de carga, cada una con sus particularidades. Ambas modalidades requieren la recopilación de información sobre las personas que conducirán, como nombres y licencias de manejo. Además, al inicio del proceso, se espera que un cliente registre ciertos datos, y en el caso de los vehículos, se debe verificar su disponibilidad.
</p>

<p align="justify">
En cuanto a la elección del lenguaje de programación, como equipo hemos decidido utilizar Python. Esta elección se basa en los conocimientos adquiridos a lo largo del trimestre, ya que hemos encontrado que Python es altamente efectivo para abordar los desafíos que surgen durante el desarrollo del código. Cuando enfrentamos dificultades, nuestro conocimiento de este lenguaje nos capacita para abordarlas de manera completa y precisa.
</p>


# ANTECEDENTES
<p align="justify">
Un servicio de transporte ofrece dos modalidades de desplazamiento: transporte de pasajeros y transporte de carga. Para cada categoría de servicio, se cuenta con una flota de vehículos específicos, cada uno diferenciado por su capacidad de transporte, ya sea de personas o de mercancías.
</p>

<p align="justify">
Los clientes que desean hacer uso de este servicio deben llevar a cabo un proceso de registro en el cual proporcionan sus datos personales, incluyendo nombre, información de identificación y datos de una tarjeta de crédito.
</p>

<p align="justify">
La reserva de un vehículo puede abarcar uno o más automóviles, especificando las fechas de recogida y entrega, así como los nombres y licencias de conducir de los individuos que se encargarán de operar dichos vehículos.
</p>

<p align="justify">
Es importante tener en cuenta que, en determinadas ocasiones, algunos vehículos podrán requerir mantenimiento en el taller, lo que conllevará a su no disponibilidad durante ciertos periodos.
</p>

# ANÁLISIS DEL PROBLEMA
<p align="justify">
En la creación de nuestro proyecto, empleamos el lenguaje de programación Python para desarrollar un sistema de "Renta de Transporte". Este sistema se basa en varias clases, incluyendo Transporte, Sistema de Transporte, Registro de Rentas, Menú, Cliente y Main. Cada una de estas clases ha sido diseñada con atributos específicos y funciones bien definidas para cumplir con su respectiva funcionalidad.
</p>

<p align="justify">
La clase "Transporte" es fundamental para determinar si un vehículo se encuentra en mantenimiento o está disponible. Además, dentro de esta clase, distinguimos dos tipos de transportes: los de pasajeros y los de carga. Esto nos permite conocer la capacidad de personas o peso, según corresponda.
</p>

<p align="justify">
La clase "Sistema de Transporte" desempeña un papel crucial al recopilar todos los datos necesarios para el proyecto. Esto incluye la solicitud de fechas de recolección y entrega, la cantidad de pasajeros, así como los datos del cliente y los detalles de la tarjeta de crédito, entre otros.
</p>

<p align="justify">
El "Registro de Rentas" se encarga de capturar la fecha de inicio y finalización de una renta, así como el nombre del cliente y su licencia de manejo.
</p>

<p align="justify">
La "Clase Menú" no posee atributos propios, ya que se centra en facilitar la creación y gestión de menús en el programa. Proporciona métodos para mostrar opciones, leer la elección del usuario y ejecutar las opciones seleccionadas.
</p>

<p align="justify">
En la clase "Cliente", se almacenan datos clave, como el nombre del cliente, su identificación, número de tarjeta de crédito, fecha de caducidad y código de seguridad.
</p>

<p align="justify">
Por último, la "Clase Main" se considera la parte principal del programa, ya que se encarga de ejecutar el código que permite obtener resultados de las clases anteriores. En resumen, cada una de estas clases cumple un rol específico en el sistema de Renta de Transporte, colaborando para su funcionamiento global.
</p>

A continuación, se proporciona el comportamiento faltante para cada una de las clases mencionadas en el proyecto de "Renta de Transporte":


- **TRANSPORTE**
  
  __* ATRIBUTOS:__
  
  - Identificador: número entero que identifica el vehículo.
  - Tipo: cadena de texto que indica si el vehículo es de pasajeros o de carga.
  - Fecha de mantenimiento: fecha en la que se programó el mantenimiento del vehículo.
  
  __* COMPORTAMIENTO:__
  
  - verificar_disponibilidad(fecha): Método que verifica si el vehículo estará disponible en la fecha proporcionada.
  - _ str _: Método que devuelve una representación en cadena del objeto.
  - guardar_datos: Método para guardar los datos del vehículo.


- **SISTEMA DE TRANSPORTE**
 
  __* ATRIBUTOS:__
  
  - vehículos: lista que almacena los objetos de vehículos, ya sean de pasajeros o de carga.
  - clientes: lista que almacena los objetos de cliente.
  - registro_rentas: lista que almacena los objetos de renta.
  - fecha_actual: variable que almacena la fecha actual.

  __* COMPORTAMIENTO:__
  
  - registro_cliente(nombre, identificacion, tarjeta): Método para registrar un nuevo cliente.
  - mostrar_vehiculos: Método que muestra una lista de los vehículos disponibles.
  - registar_renta: Método para registrar una nueva renta, solicitando datos al usuario.
  - mostrar_rentas(nombre_cliente): Método que muestra las rentas asociadas a un cliente específico.
  - registrar_vehiculo: Método para registrar un nuevo vehículo, solicitando datos al usuario.
  - cargar_datos: Método para cargar datos previamente guardados desde archivos.
  - guardar_datos(datos, lista_datos): Método para guardar datos en un archivo.
  - cambiar_fecha_actual: Método para cambiar la fecha actual del sistema.
  - menu: Método que muestra el menú principal del sistema.


- **REGISTRO DE RENTAS**
  
  __* ATRIBUTOS:__
  
  - vehículos: lista que almacena los vehículos que están relacionados con la renta.
  - fecha_inicio: variable que almacena la fecha de inicio de la renta.
  - fecha_fin: variable que almacena la fecha de finalización de la renta.
  - nombre_cliente: una cadena de texto que almacena el nombre del cliente asociado a la renta.
  - licencia_manejo: número entero que almacena el número de licencia de manejo del cliente.

  __* COMPORTAMIENTO:__
  
  - Métodos relacionados con la obtención y representación de los datos de una renta.


- **MENÚ**
  
  __* ATRIBUTOS:__
  
  No tiene atributos propios, se compone de métodos que facilitan la creación y gestión de menús en un programa, pero no define ningún atributo para almacenar información.

  __* COMPORTAMIENTO:__
  
  - mostrar_menu(opciones): Método que muestra las opciones disponibles en el menú.
  - leer_opcion(opciones): Método que lee la elección del usuario.
  - ejecutar_opcion(opcion, opciones): Método que ejecuta la opción seleccionada.
  - generar_menu(opciones, opcion_salida): Método que genera y maneja el menú principal del sistema.


- **CLIENTE**
  
 __* ATRIBUTOS:__
 
  - Nombre: cadena de texto que almacena el nombre del cliente.
  - Identificador: almacena la identificación del cliente.
  - Tarjeta crédito: cadena de texto que almacena el número de tarjeta del cliente.
  - Fecha de caducidad: fecha de vencimiento de la tarjeta junto con el código de seguridad.

  __* COMPORTAMIENTO:__
  
  - Métodos relacionados con la representación y manipulación de datos del cliente.


- **MAIN**
  
  __* ATRIBUTOS:__
  
  No tiene una clase definida, por lo que no existen atributos de una clase en particular.

  __* COMPORTAMIENTO:__
  
  - La función "main" es el punto de entrada principal del programa. Inicializa una instancia del sistema de transporte y llama al método "menú" para ejecutar el sistema y sus funcionalidades.
    
 
# DOCUMENTACIÓN

### **Registro renta:**
<p align="justify">
Esta clase permite crear objetos de registro de renta, donde cada objeto almacena información como las flechas, el nombre del cliente, la licencia de manejo y una lista de vehículos relacionados con la renta. El método "guardar_datos" permite formatear la información para ser guardada.
  
   1. Definición de la clase "RegistroRenta": representa un registro de una renta de vehículos. Esta clase tiene un contructor "_ _init_ _" y un método "guardar_datos".
      
   2. Constructor "_ _init_ _": recibe varios parámetros:
      
   - "fecha_inicio": representa la fecha de inicio de la renta.
     
   - "fecha_fin": representa la fecha de finalización de la renta.

   - "nombre_cliente": almacena el nombre del cliente asociado a la renta.

   - "licencia_manejo": guarda el número de licencia de manejo del cliente.

   - "vehículos": recibe una lista de vehículos relacionados con la renta.

*Estos parámetros se utilizan para inicializar atributos de la instancia clase:*

- "self.vehiculos" almacena la lista de vehículos.
  
- "self.fecha_inicio" guarda la fecha de inicio.
  
- "self.fecha_fin" guarda la fecha de finalización.
  
- "self.nombre_cliente" guarda el nombre del cliente.

- "self.licencia_manejo" almacena el número de licencia de manejo.

3. Método "guardar_datos":

- Formatea y devuelve una cadena de texto que representa los datos de la renta en un formato específico.

- La función "datetime.strftime" para formatear las fechas de inicio y fin con el formato "YYYY/MM/DD".

- Concatena los valores formateados junto con otros datos "nombre_cliente" y "licencia_manejo".

- Utiliza "join" para unir elementos de la lista de vehículos en una cadena, separados por "&"

- Finalmente, el método "guardar_datos" devuelve la cadena formateada conmo resultado.
  
</p>

<hr>

### **Transporte:**
<p align="justify">
Define una jerarquía de clases para representar diferentes tipos de vehículos de transporte. La clase base "Transporte" proporciona atributos y métodos comunes, y las subclases "TransportePasajeros" y "TransporteCarga" añaden atributos y métodos específicos a sus respectivos tipos de vehículos.
  
   1. Importación de "Detetime": importa las clases "detatime" del módulo "detatime", que se utilizará para trabajar con fechas.
      
   2. Clase "Transporte": definimos la clase base "Transporte"

   3. Constructor "_ _init_ _ de transporte": se inicializan tres atributos de instancia:

- "identificador": almacena un identificador único para el vehículo.
  
- "tipo_vehiculo": representa el tipo de vehículo.
  
- "fecha_mantenimiento": guarda la fecha de último mantenimiento del vehículo.

4. Método "verificar_disponibilidad de Transporte": verifica si el vehículo está disponible en una fecha dada. Compara la fecha proporcionada como argumento con la fecha de mantenimiento del vehículo. Si son diferentes, se considera que el vehículo está disponible.

5. Método "guardar_datos de transporte": se encarga de formatear los datos del vehículo y devuelve una cadena de texto con los datos separados por comas (CSV). Esto incluye el identificador, el tipo de vehículo y la fecha de mantenimiento.

6. Clase "TransportePasajeros": es una subclase de "Transporte", lo que significa que hereda las propiedades y métodos de la clase base.

7. Constructor "_ _ init _ _ de Transporte Pasajeros": inicializa los atributos de la clase base utilizando super(), y luego agrega un atributo adicional:

  - "número pasajeros": representa el número de pasajeros que el vehículo de pasajeros puede transportar.

8. Método "guardar_datos de TransportePasajeros": llama al método "guardar_datos" de la clase base utilizando super(), y luego agrega información específica de vehículos de pasajeros, como "Pasajeros" y el número de pasajeros.

9. Clase "TransporteCarga": Al igual que "TransportePasajeros", esta es una subclase de Transporte, heredando propiedades y métodos de la clase base.

10. Constructor "_ _ init _ _ " de "TransporteCarga": inicializa los atributos de la clase base usando super(), y luego agrega un atributo adicional:

- "capacidad_carga": representa la capacidad de carga en vehículos de carga.

11. Método "guardar_datos de TransporteCarga": llama al método "guardar_datos" de la clase base utilizando super(), y luego agrega información específica de vehículos de carga, como "Carga" y la capacidad de carga.
    
  
</p>

<hr>


### **MENÚ:**
<p align="justify">
Proporciona una estructura para crear y gestionar un menú interactivo en un programa, permitiendo al usuario seleccionar didefrentes ocpciones y ejecutar acciones asociadas con esas opciones.
  
1. Método "mostrar_menú": se utiliza para mostrar el menú en la consola. Recibe un diccionario de opciones como argumento, donde las claves son las selecciones posibles del menú y los valores son listas con dos elementos. El primer elemento de cada lista es la descripción de la opción, y el segundo elemento es una función que se ejecutará si se selecciona esa opción.

 - Itera a través de las claves del diccionario (opciones) ordenadas alfabéticamente utilizando "sorted(opciones)".
     
 - Muestra cada opción con su descripción utilizando "print(f' {clave}) {opciones[clave][0]}')".
      
2. Método "leer_opción": se utiliza para leer la opción seleccionada por el usuario. Recibe el mismo diccionario de opciones como argumento.

- Muestra el mensaje "Opción: " y espera a que el usuario ingrese una opción.
     
- Utiliza una expresión walrus (:=) para asignar lo que el usuario ingresó a la variable "opción" y al mismo tiempo verifica si esa opción está en el diccionario de opciones (opción not in opciones).
     
- Si la opción no está en el diccionario, muestra el mensaje "Opción incorrecta, vuelva a intentarlo." y continúa esperando a que el usuario ingrese una opción válida.
     
- Una vez que el usuario ingresa una opción válida, devuelve esa opción.

3. Método "ejecutar_opción":  se utiliza para ejecutar la función asociada a la opción seleccionada. Recibe la opción seleccionada y el diccionario de opciones como argumentos.

- "identificador": almacena un identificador único para el vehículo.
  
- "tipo_vehiculo": representa el tipo de vehículo.
  
- "fecha_mantenimiento": guarda la fecha de último mantenimiento del vehículo.

4. Método "generar_menú": se utiliza para generar y gestionar el menú completo, incluyendo la lectura de opciones, ejecución de acciones y repetición del proceso hasta que el usuario elija una opción de salida. Recibe el diccionario de opciones y una opción de salida como argumentos.

   - Inicializa la variable "opcion" como "None".
  
   - Entra en un bucle while que se ejecutará hasta que la opción seleccionada sea igual a la opción de salida.
  
   - En cada iteración del bucle:
     
   - Llama al método "mostrar_menu" para mostrar el menú.
    
   - Llama al método "leer_opcion" para que el usuario ingrese una opción válida.
    
   - Llama al método "ejecutar_opcion" para ejecutar la función asociada a la opción seleccionada.
    
   - Muestra una línea en blanco (print()) para separar las iteraciones del menú.
    
  
</p>

<hr>

### **CLIENTE:**
<p align="justify">
Permite crear instancias de clientes con sus atributos iniciales y proporciona un método para obtener una representación de los datos del cliente en un formato específico.
  
1. Método "_ _ init _ _: se ejecuta cuando se crea una nueva instancia de la clase "Cliente". Recibe tres argumentos: "nombre", "identificacion", y "tarjeta_credito".

 - "nombre", "identificacion", y "tarjeta_credito" son atributos de la instancia que se inicializan con los valores pasados como argumentos. Estos atributos representan el nombre, identificación y número de tarjeta de crédito del cliente..
     
 - Los atributos "self.nombre", "self.identificacion", y "self.tarjeta_credito" almacenan los valores de los argumentos en la instancia del cliente. Estos atributos permiten acceder a la información del cliente más adelante en el programa..
      
2. Método "guardar_datos": se utiliza para gauardar los datos del cliente:

- El método devuelve una cadena que contiene la información del cliente en un formato específico. En este caso, la información se concatena utilizando comas (",").
     
- La información del cliente se compone de tres partes: el nombre, la identificación y el número de tarjeta de crédito. Estas partes se concatenan utilizando "+" y se separan por comas.
     
- Finalmente, se devuelve la cadena con los datos del cliente.
    
  
</p>

<hr>







