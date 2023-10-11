[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/XixB-tii)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12235114)

![uamcua](https://github.com/AGN-Teaching/practica-3-entrada-y-salida-daniii2012/assets/125592302/bdd3b460-bc5c-42c1-953e-cb74450174dd)

# PROYECTO FINAL
UNIVERSIDAD AUTÓNOMA METROPOLITANA  "UNIDAD   CUAJIMALPA"
# RENTA DE TRANSPORTE
LICENCIATURA: INGENIERÍA EN COMPUTACIÓN 


UEA: *PROGRAMACIÓN ORIENTADA A OBJETOS*



*ESTUDIANTE:*


- Daniela Nava Martínez                 2223028762
- Anaid Olguin Rico                     2203024973
- Jesús Emmanuel Ramírez Aguilera       2223068873

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
Para la elaboración de nuestro proyecto, hemos empleado el lenguaje de programación Python con el propósito de desarrollar la aplicación "Renta de Transporte". Como se mencionó previamente, hemos empleado diversas clases en este proyecto, a saber: "Tarjeta de Crédito", "Cliente", "Persona", "Transporte", "Vehículo" y "Main". Cada una de estas clases ha sido concebida con atributos específicos y una función definida.
</p>

<p align="justify">
La elección de la clase "Tarjeta de Crédito" reviste una importancia fundamental, ya que esta requiere los datos de una tarjeta de crédito para llevar a cabo el proceso de contratación del servicio. La clase "Cliente", por su parte, ostenta un rol preponderante, ya que la consideramos como el actor principal que inicia el proceso de solicitud del servicio.
</p>

<p align="justify">
La clase "Persona" se ha concebido con el propósito de registrar el nombre y la identificación de la persona que fungirá como el conductor del vehículo. Por otro lado, la clase "Transporte" cumple con la función de recopilar datos relativos al vehículo, incluyendo las fechas de solicitud y entrega del automóvil, además de los datos del conductor.
</p>
  
<p align="justify">
La clase "Vehículo" adquiere un papel crucial en el proyecto al permitirnos distinguir entre vehículos de pasajeros y de carga, especificando sus capacidades y su disponibilidad. Por último, la clase "Main" actúa como la entidad principal desde la cual se ejecutan todas las operaciones y procesos del código, lo que culmina en el registro de la solicitud de servicio. A continuación, procederemos a ofrecer una descripción más detallada de cada una de estas clases.
</p>
