# Future versions
El proyecto de gestión de ticketes contará con avances y nuevas características a medida que el tiempo transcurra. Es por esto que mediante este documento se mostrarán las posibles nuevas implementaciones o cambios para el mismo

# Añadir función de borrado.
El sistema de tickets a día de hoy no cuenta con la funcionalidad de borrar un ticket, la cuál es casi imprescindible para cuando la cantidad de los mismos sea muy grande, debería de contar con la opción de borrar un ticket conociendo su ID o bien eliminar todos los tickets según su autor,fecha, etc.

Es también de una decisión a futuro decidir si el borrado del ticket elminará completamente el registro, o si será mejor implementar un *soft - delete* dependiendo de la importancia del guardado de los mismos para el sistema.

# Mejorar el ingreso de los comandos
El ingreso de los comandos por la terminal en el sistema puede ser confuso para los usuarios, es por esto que surge la posible tarea de migrar toda la lógica de ingreso de los comandos a librerías de *python* más modernas, como lo pueden ser *ArgumentParser*, o *shlex* que nos permiten definir argumentos de una manera más visual para el usuario y brindan la posibilidad de definir las diferentes ayudas para los comandos.
# Mejorar la creación de un ticket implementando sesiones.
Actualmente, en el sistema, cualquier usuario puede crear un ticket añadiendo cualquier valor en el campo de autor, es por esto que una nueva funcionalidad debe ser la de auntentificador de los clientes que se conecten, la cuál modificará a su vez la funcionalidad de otros comandos *Ejemplo*: *Al añadir un ticket nuevo, el autor debe ser el usuario autentificado.*
# Migrar sockets a ZMQ
[![N|Solid](https://zeromq.org/images/logo.gif)](https://zeromq.org/languages/python/)


ZeroMQ es una herramienta que nos permite resolver problemas frecuentes que ocurren al utilizar los sockets de python, nos permite definir sockets del tipo publicadores, subscriptores como también conectarnos a canales de eventos, entre otros.

# Desarrollar funcionalidad web
Si la escalabilidad del proyecto aumentase, será necesario introducir funcionalidad para que los usuarios, desde un navegador puedan realizar las mismas operaciones como se hacen en una terminal.





