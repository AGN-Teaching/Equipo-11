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
El propósito principal de este proyecto es desarrollar un servicio de transporte que ofrece dos modalidades: transporte de pasajeros y transporte de carga,cada una con sus particularidades. Ambas modalidades requieren la recopilación de información sobre las personas que conducirán, como nombres y licencias de manejo. Además, al inicio del proceso, se espera que un cliente registre ciertos datos, y en el caso de los vehículos, se debe verificar su disponibilidad.
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
En la creación de nuestro proyecto, empleamos el lenguaje de programación Python para desarrollar un sistema de "Renta de Transporte". Este sistema se basa en varias clases, incluyendo Transporte, Sistema de Transporte, Rentas, Menú, Cliente y Main. Cada una de estas clases ha sido diseñada con atributos específicos y funciones bien definidas para cumplir con su respectiva funcionalidad.
</p>

<p align="justify">
La clase "Transporte" es fundamental para determinar si un vehículo se encuentra en mantenimiento o está disponible.Dentro de esta clase se encuentran los atributos de nuestros transportes, un identificador para facilitar la busqueda y solicitud de los vehiculos, asi como el tipo de vehiculo a rentar  y las fechas de mantenimiento en donde no se encontraran disponibles.Además, dentro de esta clase, distinguimos dos tipos de transportes: los de pasajeros y los de carga. Esto nos permite conocer la capacidad de personas o peso, según corresponda.
</p>

<p align="justify">
La clase "Sistema de Transporte" desempeña un papel crucial al recopilar todos los datos necesarios para el proyecto. Esto incluye la solicitud de fechas de recolección y entrega, la cantidad de pasajeros, así como los datos del cliente y los detalles de la tarjeta de crédito, esta clase tambien nos permite de manera manual ingresar datos de vehiculos, asi como subirlos directamente de un archivo de texto y guardarlos para su posterior uso. 
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
</p>

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


- **RENTA**
  
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
    

# DIAGRAMA UML

<p align="justify">
El diagrama UML proporcionan una representación visual de las clases, objetos, relaciones y estructuras del sistema, lo que facilita la comprensión y la comunicación entre los desarrolladores y otras partes interesadas.
</p>

![uml_transporte](https://github.com/AGN-Teaching/Equipo-11/assets/125592302/d1cd5347-59ce-4e81-bfaf-dac6c5e3ddae)

### **Diagrama UML "Cliente":**

![cliente](https://github.com/AGN-Teaching/Equipo-11/assets/125592302/4ca38152-a813-4b4c-94e5-3d27f32b944d)

<p align="justify">
  
- La clase se llama "cliente".

- Tiene tres atributos: "nombre", "identificación" y "tarjeta" todos de tipo string.

- Cuenta con un constructor (_ _ init _ _) que toma tres parámetros: "nombre", "identificación" y "tarjeta" y les asigna atributos correspondientes.

- Tiene un método llamado "guardar_datos" no toma argumentos y devuelve una cadena (str). Retorna una representación en forma de cadena de los atributos del cliente.
    
</p>

<hr>


### **Diagrama UML "Renta":**

![renta](https://github.com/AGN-Teaching/Equipo-11/assets/125592302/c1681b2d-ed7d-49da-8316-d1197d3ac9ae)


<p align="justify">
  
- La clase se llama "renta".

- Tiene cinco atributos: "fecha_inicio", "fecha_fin", "nombre_cliente", "licencia manejo" y "vehículos".

- Cuenta con un constructor (_ _ init _ _) que toma cinco parámetros y asigna esos valores a los atributos correspondientes.

- Tiene un método llamado "guardar_datos" no toma argumentos y devuelve una cadena (str).
    
</p>

<hr>


### **Diagrama UML "transporte":**

![transporte](https://github.com/AGN-Teaching/Equipo-11/assets/125592302/3aa097c2-d140-4fa2-a236-7555f0a1e5c8)



<p align="justify">
  
- La clase "transporte" tiene tres atributos: "identificador", "tipo vehículo" y "fecha_mantenimiento". Tamnién tiene dos métodos "verificar_disponibilidad(fecha)" y "guardar_datos()".

- La clase "TransportePasajeros" hereda de "Transporte" e introduce un nuevo atributo, "numero_pasajeros" de tipo "int". Anula el método "guardar_datos() para incluir información adicional específica de pasajeros.

- La clase "TransporteCarga" hereda de "Transporte" e introduce un nuevo atributo, "capacidad_carga". Anula el método "guardar_datos() para incluir información adicional específica de carga. 
    
</p>

<hr>

### **Diagrama UML "sistema transporte":**

![sistematransporte](https://github.com/AGN-Teaching/Equipo-11/assets/125592302/a73bb981-5299-41ff-8ef2-8f7a781fc2ae)


<p align="justify">
  
- La clase "SistemaDeTransporte" tiene varios atributos, incluyendo la lista para almacenar "vehículos", "clientes", "registro_renta", así como la "fecha_actual". Tiene varios métodos, como registro_ciente(), mostrar_clientes(), vehiculo_disponible(), mostrar_vehiculos(), solicitar_vehiculos(), registrar_renta(), mostrar_rentas(), registrar_vehiculo(), cargar_datos(), guardar_datos(), y menu(). 

- La clase "Menú" no se muestra explícitamente en el diagrama, pero se utiliza para mostrar un menú de opciones y ejecutar acciones en función de la elección del usuario.

- Las clases "Cliente", "Renta", "TransporteCarga", y "TransportePasajeros" son utilizadas en el código, pero no están incluidas en el diagrama. Estas clases contienen atributos y métodos relacionados con sus respectivas entidades.
    
</p>

<hr>


### **Diagrama UML "menú":**

![menu](https://github.com/AGN-Teaching/Equipo-11/assets/125592302/c8463864-9767-4da2-87fc-bafeb419dbeb)



<p align="justify">
  
- La clase "Menu" contiene cuatro métodos: 

  - "mostrar_menu(opciones): Muestra un menú de opciones en la consola. Toma un diccionario de opciones como entrada y muestra cada opción numerada con su descripción.
 
  - "leer_opcion(opciones): Permite al usuario seleccionar una opción ingresando un número. Verifica si la opción ingresada está en el diccionario de opciones y continúa solicitando una opción válida hasta que se ingrese una opción válida.
 
  - ejecutar_opcion(opcion_opciones): Ejecuta la acción asociada con la opción seleccionada. Toma la opción seleccionada como entrada y busca la acción correspondiente en el diccionario de opciones para ejecutarla.
 
  - generar_menu(opciones, opcion_salida): Genera un bucle que muestra el menú, lee la opción del usuario, ejecuta la acción correspondiente y repite hasta que se ingrese la "opción de salida" (generalmente usada para salir del menú).
    
</p>

<hr>


# RELACIONES ENTRE CLASES

<p align="justify">
Se refieren a cómo las clases interactúan y se relacionan entre sí dentro de un sistema de software. Estas relaciones son fundamentales para modelar y construir sistemas complejos. Las relaciones entre clases pueden ser de varios tipos, incluyendo:

- Generalización/Especialización (herencia): Representa una relación jerárquica entre una clase base (superclase) y una clase derivada (subclase). La subclase hereda atributos y métodos de la superclase y puede extender o sobrescribir sus comportamientos.

- Asociación: Representa una relación estructural entre dos clases, donde una clase utiliza o referencia a la otra. Puede ser una asociación simple o una asociación más fuerte como la agregación o la composición.

- Agregación: Representa una relación de "todo a parte" donde una clase contiene o se compone de otras clases. Las partes pueden existir por sí mismas y se pueden compartir entre varias instancias de la clase contenedora.

- Composición: Es una forma más fuerte de agregación donde las partes están fuertemente ligadas a la clase contenedora. En una composición, las partes no pueden existir sin la clase contenedora.
</p>

![relacion](https://github.com/AGN-Teaching/Equipo-11/assets/125592302/301a3a32-3c3c-4ac5-aef8-56e1490fca83)

<p align="justify">
  
  1. Sistema Transporte.

  - Es el componente principal que interactúa con las otras clases para gestionar el sistema de alquiler de vehículos.
    
  - Utiliza la clase Menú para crear un menú interactivo para el usuario.

  - Tiene relaciones de composición con las clases Cliente, Renta y las clases derivadas de Transporte (almacena clientes, registros de rentas y vehículos).


  2. Renta.

  - Se encarga de representar una transacción de alquiler de vehículos.

  - Puede o no tener una relación de composición con la clase Cliente, ya que almacena el nombre del cliente en la renta.**


  3. Cliente.

  - Representa a un cliente y almacena información como su nombre, identificación y tarjeta de crédito.

  - No presenta relaciones directas con otras clases.


 4. Menú.

  - Se encarga de interactuar con el usuario y proporciona un menú de opciones.

  - No presenta relaciones directas con las otras clases. Su función es proporcionar una interfaz de usuario para interactuar con el sistema.


 5. Transporte.

  - Representa vehículos en general y contiene propiedades como identificador, tipo de vehículo y fecha de mantenimiento.

  - Las clases "TransportePasajeros" y "TransporteCarga" heredan de la clase Transporte, lo que establece una relación de herencia. Estas clases especializadas heredan propiedades y métodos de la clase base.
    
</p>


# DOCUMENTACIÓN

### **Renta:**
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


### **Menú:**
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

### **Cliente:**
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


### **Sistema transporte:**
<p align="justify">
Se utiliza para gestionar un sistema de registro y renta de  vehículos, interactuando con clientes, vehículos y rentas. La clase incluye métodos para registrar clientes, vehículos, rentas, cargar y guardar datos, y presentar un menú de opciones para el usuario.
  
1. Importaciones de módulos: El código comienza importando varios módulos que son utilizados en el programa. Estos módulos incluyen datetime para trabajar con fechas y horas, así como varios módulos personalizados: "Cliente", "RegistroRenta", "Transporte", "TransporteCarga", "TransportePasajeros" y "Menu".

2. Definición de la clase "SistemaDeTransporte": encapsula la funcionalidad del sistema de registro y renta de vehículos.

3. Método "_ _ init _ _": se llama cuando se crea una instancia de la clase. En este caso, inicializa los atributos de la instancia:

   - "self.vehiculos", "self.clientes" y "self.registro_rentas" son listas que almacenan objetos de vehículos, clientes y registros de alquiler, respectivamente.
  
   - "self.fecha_actual" almacena la fecha y hora actuales obtenidas mediante "datetime.now()".
  
4. Método "solicitar_fecha": permite solicitar al usuario una fecha con un mensaje (prompt) y validar que la fecha ingresada tenga el formato correcto (YYYY/MM/DD). Retorna un objeto de fecha datetime si la entrada es válida.

5. Método "fecha_to_str": convierte un objeto de fecha "datetime" en una cadena de texto con el formato "YYYY/MM/DD".

6. Método "registro_cliente": permite registrar un nuevo cliente. Solicita al usuario el nombre, identificación y número de tarjeta de crédito y crea una instancia de la clase "Cliente", luego la agrega a la lista de clientes.

7. Método "mostrar_cliente": muestra en la consola una lista de los clientes registrados junto con su nombre, identificación y número de tarjeta de crédito.

8. Método "vehículo_disponible": verifica si un vehículo está disponible para ser rentado en una fecha específica. Puede mostrar solo vehículos disponibles si "solo_mostar_disponibles" es "True".

9. Método "mostrar_vehículos":  muestra en la consola una lista de vehículos registrados, con detalles como su identificación, tipo, fecha de mantenimiento, capacidad de pasajeros o capacidad de carga, según el tipo de vehículo. Puede mostrar solo vehículos disponibles si "solo_mostar_disponibles" es "True".

10. Método "solicitar_vehículos": permite al usuario seleccionar vehículos para rentar. Muestra una lista de vehículos disponibles y permite al usuario seleccionar uno o más vehículos. Retorna una lista de identificadores de vehículos seleccionados.

11. "Método registrar_renta": permite al usuario registrar una renta de vehículos. Solicita fechas de recolección y entrega, nombre del cliente, licencia de manejo y vehículos a alquilar.

12. Método "mostrar_rentas": muestra en la consola una lista de las rentas registradas, con detalles como el nombre del cliente, licencia de manejo y fechas de recolección y entrega.

13. Método "registrar_vehículo": permite al usuario registrar un nuevo vehículo. Solicita el identificador, tipo, fecha de mantenimiento y tipo de vehículo (pasajero o carga), y agrega el vehículo a la lista de vehículos.

14. Método "cargar_datos": carga datos previamente guardados desde archivos. Lee información de clientes, vehículos y rentas desde archivos de texto y almacena estos datos en las listas correspondientes.

15. Método "guardar_datos": guarda los datos de clientes, vehículos y rentas en archivos de texto para su posterior recuperación.

16. Método "menú": muestra un menú de opciones y permite al usuario interactuar con el programa. Incluye registrar clientes, mostrar clientes, mostrar vehículos, registrar rentas, mostrar rentas, registrar vehículos, guardar datos, cargar datos y salir.
    
  
</p>

<hr>

### *Main:*
<p align="justify">
Este código configura y ejecuta el sistema de transporte definido en la clase "Sistema de Transporte" cuando se ejecuta como un programa independiente.

1. Importación de "SistemaDeTransporte": importa la clase "SistemaDeTransporte" desde el módulo "sistemadetransporte". Esto significa que el código en "SistemaDeTransporte" esta disponible para su uso en este archivo.

2. Función "main": es el punto de entrada principal para el programa. Dentro de la función:

- Se crea una instancia de la clase "SistemDeTransporte" y se almacena en una variable llamada "sistema".

- Luego, se llama al método "menú" de la instancia "sistema". Inicia la funcionalidad del sistema de transporte y muestra un menú interactivo.

3. Bloque "if _ _ name _ _" = = "_ _ main _ _": es una estructura condicional que comprueba si el script se está ejecutando como un programa independiente o si se está importando como un módulo en otro script. Cuando ejecutas este script directamente, _ _ name _ _ se establece en "_ _ main _ _". Por lo tanto, el bloque de código dentro de if _ _ name _ _ == "_ _ main _ _": se ejecutará solo si el script se ejecuta como un programa independiente.

Dentro de este bloque, se llama a la función "main()", que inicia la ejecución principal del programa. Esto significa que cuando ejecutas este archivo como un programa, se creará una instancia del sistema de transporte y se mostrará su menú interactivo.
</p>

<hr>


# CONVENCIONES DEL LENUAJE DE PROGRAMACIÓN

<p align="justify">

1. __CLIENTE__

   - La clase "Cliente" sigue las convenciones de nomenclatura, con un constructor "_ init _" para inicializar los atributos y un método "guardar_datos" para devolver una representación en cadena de la instancia.
  
2. __RENTA__

   - La clase "Renta" sigue las mismas convenciones de nomenclatura, con atributos para almacenar información de la renta y un método "guardar_datos" para devolver una representación en cadena.
  
3. __TRANSPORTE__

   - La clase "Transporte" utiliza las convenciones de nomenclatura y proporciona un método para verificar la disponibilidad del vehículo en una fecha determinada.
  
   - Las clases derivadas, como "TransportePasajeros" y "TransporteCarga", siguen las mismas convenciones y agregan atributos específicos para su tipo de vehículo, con métodos para guardar datos de manera específica.   


4. __MENÚ__

   - La clase "Menu" se encarga de mostrar un menú de opciones, leer la elección del usuario y ejecutar las acciones asociadas a esas opciones.
  
     
5. __SISTEMA DE TRANSPORTE__

   - La clase "SistemaDeTransporte" es la clase principal que gestiona clientes, vehículos, rentas y proporciona funcionalidades como la carga y guardado de datos. También se encarga de mostrar un menú para interactuar con el sistema.

  
6. __MAIN__

   - La función "main()" se encarga de crear una instancia de "SistemaDeTransporte" y ejecutar el menú principal.

</p>

<p align="justify">
  Todos los código siguen las concenciones de Python y utilizan las clases y métodos para organizar y gestionar relacionados con un sistema de transporte. Cada clase tiene atributos y métodos apropiadamente nombrados, lo que hace ser más comprendible el código.
</p>

# CONCLUSIONES:

__NAVA MARTINEZ DANIELA:__ 





__OLGUIN RICO ANAID:__
+ La programacionn orientada a objetos nos proporciona una forma estructurada y modular para resolver nuestros problemas.
+ Facilita la creacion y el mantenimiento del codigo.
+ La herencia y polimorfismo nos ayudan a reutilizar codigo al heredar atributos y metodos de una clase padre a una o varias clases hijas, asi estas aprovechan la funcionalidad de la clase padre.
+ A traves del desarrollo del programa se pueden encontrar mejoras para el funcionamiento del sistema y gracias al diseño modular estas mejoras pueden añadirse apoyandose del codigo existente, y hacer pruebas sin afectar el mismo. 
+ El diseño de un programa orientado a objetos requiere una buena comprension del problema a desarrollar, ya que puede tener ambiguedades debido al lenguaje que usemos al definir nuestros objetos.



__RAMIREZ AGUILERA JESUS EMMANUEL:__
+ La culminación de nuestro proyecto de Programación Orientada a Objetos representa la aplicación exitosa de los conceptos esenciales que hemos aprendido durante el trimestre. Hemos incorporado eficazmente el polimorfismo, la herencia, las clases y subclases en el diseño de un servicio de transporte que ofrece modalidades tanto de pasajeros como de carga, cada una adaptada a sus propias necesidades.

+ La elección de Python como nuestro lenguaje de programación fue fundamental, ya que nuestra familiaridad con este lenguaje nos permitió abordar los desafíos con eficiencia y precisión. La programación orientada a objetos nos brindó una estructura modular que facilita el desarrollo y la mejora continua del sistema. La herencia y el polimorfismo permitieron la reutilización de código de manera efectiva, mientras que los diagramas UML brindaron una representación visual clara de las clases y sus relaciones, mejorando la comunicación entre los desarrolladores y partes interesadas.

+ Este proyecto nos ha enseñado la importancia de comprender a fondo el problema a resolver y cómo modelar clases y sus relaciones de manera efectiva. Las relaciones entre clases, como la generalización, asociación, agregación y composición, se han convertido en una parte integral de nuestro enfoque en la construcción de sistemas de software complejos.

+ En conclusión, nuestro proyecto de Programación Orientada a Objetos ha demostrado que podemos aplicar con éxito los conceptos y herramientas aprendidos en el curso para abordar problemas del mundo real de manera efectiva y estructurada.





