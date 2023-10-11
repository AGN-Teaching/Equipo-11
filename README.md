[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/XixB-tii)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12235114)

![uamcua](https://github.com/AGN-Teaching/practica-3-entrada-y-salida-daniii2012/assets/125592302/bdd3b460-bc5c-42c1-953e-cb74450174dd)

# PROYECTO FINAL
UNIVERSIDAD AUTÓNOMA METROPOLITANA  "UNIDAD   CUAJIMALPA"
# RENTA DE TRANSPORTE
LICENCIATURA: INGENIERÍA EN COMPUTACIÓN 


UEA: *PROGRAMACIÓN ORIENTADA A OBJETOS*



*ESTUDIANTE:*


Daniela Nava Martínez                MATRÍCULA: 2223028762


Jesús Emmanuel Ramírez Aguilera      MATRÍCULA: 2223068873


Anaid Olguin Rico                    MATRÍCULA: 2203024973

*PROFESOR:* 


Abel García Nájera


# RESUMEN
La Práctica 3 de la (UEA) "Programación Orientada a Objetos" se enfoca en la aplicación de los conceptos adquiridos durante las clases, específicamente en el ámbito de la **Entrada y Salida de Datos**, con la ayuda del diseño de **diagramas UML**. Estos diagramas desempeñan un papel fundamental al proporcionarnos una representación visual de las clases, sus atributos, tipos y las firmas de los métodos.


El objetivo principal de esta práctica consiste en desarrollar un **servicio de streaming** utilizando los conocimientos previamente adquiridos en la práctica 2. En esta ocasión, se incorporará un menú principal que contendrá diversas opciones, junto con un menú de administrador que permitirá agregar un video, eliminar un video, mostrar el catálogo, cargar el catálogo y guardar el catálogo. También se incluirá un menú para el cliente. Los diagramas UML son una herramienta invaluable que facilita la identificación de las clases y subclases, agilizando así el proceso de codificación.


En la tercera práctica, al igual que en las anteriores, **opté por utilizar Python** en lugar de Java como lenguaje de programación. Esta decisión se basó en mi elección inicial de utilizar Python desde el principio y en la percepción de que Python ofrece una mayor facilidad para abordar ciertos desafíos que surgen durante el desarrollo del código en comparación con Java, además de que su interfaz es un poco más sencilla. Esta elección me permitió resolver problemas de manera más eficiente y efectiva en el contexto de la práctica.



# ANTECEDENTES
Un servicio de streaming requiere un sistema esencial para administrar su contenido. Los videos disponibles en el catálogo del servicio se dividen en tres categorías principales: películas, series y documentales. Cada video, sin importar la categoría, cuenta con un identificador único, título, director, clasificación, año de lanzamiento, cantidad de calificaciones recibidas y calificación promedio. Además, cada categoría tiene información específica adicional:


- *Película:* Actriz o actor principal y duración.


- *Serie:* Número de temporadas y número de episodios.


- *Documental:* Tema y productor.


El sistema debe tener dos tipos de usuarios: administradores y clientes. El subsistema para los administradores debe permitirles agregar nuevos videos al catálogo, eliminar videos del catálogo, cargar el catálogo desde un archivo y guardar el catálogo en un archivo. Por otro lado, el subsistema para los clientes debe permitirles calificar videos y reproducirlos. Ambos tipos de usuarios tienen la opción de ver el catálogo completo de videos.


Todas estas acciones pueden realizarse a través de un conjunto de menús que se detallan a continuación.

- **Menú principal**
1. Administrador
2. Cliente
3. Salir


- **Menú administrador**
1. Agregar un video
2. Eliminar un video
3. Mostrar el catálogo
4. Cargar catálogo
5. Guardar catálogo
6. Regresar


- **Agregar un vídeo**
1. Película
2. Serie
3. Documental
4. Regresar


- **Eliminar un vídeo**
Para eliminar un video, es necesario que el administrador introduzca la información que identifique de forma única el video que desea eliminar.


- **Mostrar catálogo**
Esta opción desplegará el contenido del catálogo, el cual muestra, para cada video, además del identificador, título, categoría, el número de veces que se ha reproducido y el promedio de las calificaciones recibidas, la información respectiva a la categoría.


- **Cargar catálogo**
El sistema solicitará el nombre del archivo en donde está almacenado el catálogo. Si el archivo existe y se puede leer, se cargará el contenido del mismo.


- **Guardar catálogo**
El sistema solicitará el nombre del archivo en donde se guardará el catálogo. Si el archivo se puede abrir para escritura, se guardarán los datos de los productos. Esta acción debe considerar el concepto de persistencia de objetos.


- **Menú cliente**
1. Reproducir un video
2. Calificar un video
3. Mostrar el catálogo
4. Regresar


- **Reproducir un vídeo**
Para reproducir un video, es necesario que el cliente introduzca la información que identifique de forma única el video que desea reproducir.


- **Calificar un vídeo**
Para calificar un video, es necesario que el cliente introduzca la información que identifique de forma única el video que desea calificar y, posteriormente, su calificación.


- **Mostrar catálogo**
Esta opción desplegará el contenido del catálogo, el cual muestra para cada video, además del identificador, título, categoría, el número de veces que se ha reproducido y el promedio de las calificaciones recibidas, la información respectiva a la categoría.


# DOCUMENTACIÓN

__CÓDIGO VÍDEOS__

*- class Video:* Define una clase llamada Video que representa un objeto de video.

*- def __init__(self, id, titulo, director, clasificacion, estreno, calificaciones, promedio):* Define el constructor de la clase Video para inicializar sus atributos.

Se definen los métodos obtener_id, establecer_id, obtener_titulo, establecer_titulo, obtener_director, establecer_director, y así sucesivamente, para acceder y modificar los atributos de la clase.
