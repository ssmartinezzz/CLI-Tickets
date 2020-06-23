# Readme Info
En este arhivo se justificará la elección de las diferentes herramientas, tecnologías, módulos entre otros desde una perspectiva teorico -práctica.


# Justificación de Tipo de protocolo de transporte
Una de las exigencias de este proyecto, fue que el establecimiento de las conexiones para el envío de datagramas IP fuera utilizando **Sockets INET stream** que los cuales se implementan en python de la siguiente manera importando el módulo socket.
```sh
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
El porque de la implementación de estos sockets, es que principalmente utilizan el protocolo de transporte **TCP** *(Transfer Control Protocol)*, el cuál se caracteríza por garantizar la entrega de los paquetes o en este caso denominado *segmentos* a los extremos de la conexión, es decir, a los clientes, como al servidor.
Un socket básicamente esta formado por una dirección IP y un determinado número de puerto. Esto permite la multiplxeación del sistema, es decir, poder conectar multiples clientes a una misma dirección de servidor, cosa que el protocolo IP no puede realizar de por sí solo.

Otra carecterística propia del protocolo, que se vió sobre la implementación de sockets en el proyecto fue los usos de los **mecanismos de control de flujo y congestión**, porque para no saturar la ventana de recepción de los sockets en el código se le estableció de la siguiente manera:

```sh
socket.recv(1024)
```
# Elección del tipo de base de datos (Relacional)
![N|Solid](https://serv3.raiolanetworks.es/blog/wp-content/uploads/mysqloptimizar1.png)

Princiaplmente se optó por elegir una base de datos del tipo relacional, como es el caso del lenguaje **SQL** con MySQL porque al ser del tipo *Modelo ENTIDAD - RELACIÓN* nos permite relacacionar tablas entre sí de una base de datos, en este proyecto solo se cuenta con una única entidad la cual es Ticket, si el alcance y la complejidad del proyecto aumentacen en un futuro, no resultaría difícil agregar otras entidades y relacionarlas entre sí.

Entre las principales **Ventajas** de la utilización de un Modelo relacional de base de datos tenemos que
  - Provee herramientas que garantizan evitar la duplicidad de registros.
  - Garantiza la integridad referencial, así, al eliminar un registro elimina todos los registros relacionados dependientes.
  - Favorece la normalización por ser más comprensible y aplicable.

# Justificación de la implementación de THREADING
Para poder multiplexar las conexiones el servidor, se estableció como requisito que el hilo principal de [server.py](https://gitlab.com/s.martinez/tickets/-/blob/master/server.py) inicialice un nuevo por cada cliente que se conecte. A su vez, el módulo *threading* de python posee mecanismos para controlar el funcionamiento de estos hilos.
Este es el caso, de la implementación de la función lock *(O cierre en español)* que su implementación sirvió para blockear a 2 hilos de subir tickets a la base de datos exactamente al mismo instante.
# Justificación del módulo multiprocessing.
El módulo multiprocessing fue de suma importancia en este proyecto, ya que tiene dentro la función **Process()** la cuál nos permite generar un proceso paralelo, la ventaja de esto es que el desde el lado del cliente, si agregaran diferentes funcionalidades a la tarea de exportar un ticket, se podrían realizar las 2 partes (o procesos) que involucren a la tarea exactamente en el mismo momento, como esta tarea actual no consiste de mucha complejidad, es dificil de percibir el procesamiento en paralelo trabajando en los diferentes núcleos del procesasdor. 

  
