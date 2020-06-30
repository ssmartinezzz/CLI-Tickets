# Sistema de gestión de tickets por CLI

Para el correcto funcionamiento, este sistema requiere llevar a cabo una serie de pasos.

Se debe tener en cuenta que el sistema esta desarrollado para **MySQL** por lo que es requisito para su correcto funcionamiento tener instalado el mismo.

También se debe tener en cuenta que ciertos módulos deben ser instalados en el entorno virtual como lo son: *PyMYSQL*, *python-doenv* entre otros.

# Etapa 1: Creación de un entorno virtual
Si ya usted ya posee Python instalado en su computadora, usted ya puede contar con las funcionalidades que el mismo posee, una de ellas es la creación de un entorno virtual, permitiendo instalar diferentes módulos sin afectar el funcionamiento general.
  - Realizar un entorno virtual a un directorio ya existente (Linux)
  ```sh
$ cd path/directorio
$ pyhton3 -m venv .
```
Una vez creado dicho directorio se muestran 2 alternativas:
   - Activarlo: 
 ```sh
$ cd path/directorio
$ source bin/activate
(directorio) ordenador@xx:path_directorio$
```
- Desactivarlo:
 ```sh
$ cd path/directorio
$ source bin/deactivate
(directorio) ordenador@xx:path_directorio$
```
# Etapa 2: Clonación del repositorio
Para obtener una copia del sistema, es necesario clonar el mismo para ello se debe:
 - Vistitar url del repositorio [Repositorio](https://gitlab.com/s.martinez/tickets)
 - Copiar el enlace del boton *clone with https*
 - Ir al directorio en el cual se creo el *entorno virtual* y desde la terminal ejecutar
 
 ```sh
$ git clone https://gitlab.com/s.martinez/tickets.git
``` 
 Asi obteniendo todos los archivos necesarios para la ejecución del sistema.
# Etapa 3: Instalación del ORM SQLAlchemy
Este ORM nos permite relacionar modelos y entidades de base de datos, como la ejecución de sentencias de lenguaje SQL, entre otros. Para instalarlo se debe
 - Activar el entorno virtual
 - Una vez activado, ejecutar el comando  `$pip3 install SQLAlchemy`
 
# Etapa 4: Exportación de las credenciales de MySQL
Por razones de seguridad para el usuario es necesario que ciertas credenciales no queden visibles en el código, es por esto que se debe crear un archivo local que las contenga:
 ```sh
$ source bin/activate
(directorio) ordenador@xx:path_directorio$ touch .env
```
Una vez creado, debemos acceder al mismo para exportar las credenciales, si el archivo no está visible, se debe recordar mostralo con `Ctrl + h`

Para exportar las credenciales, deberá acceder al archivo y agregar las variables:
`export DB_USERNAME=nombre_usuario_MySql`
`export DB_PASS=contraseña_Mysql`

El siguiente paso correspondiente es **Crear el schema o Base** en MySQL, una vez realizado esto, se debe especificar el nombre y localización de la misma en el archivo *dbConfiguration.py*

Una vez creada la base de datos o *schema* **MySQL** se debe proceder a ejecutar el archivo *models.py* el cuál se encargará de las tablas en la base de datos que se especificó en el archivo de *dbConfiguration.py*


### Ejecución básica
La explicación detallada de los comandos aplicables, está detallada en el archivo de README, aquí se especificará los detalles primordiales para poder lanzar el cliente y el servidor.

Para lanzar el servidor se debe estar en el directorio de los archivos con el *entorno virtual* encendido y ejecutar en una terminal
 ```sh
$ source bin/activate
(directorio) ordenador@xx:path_directorio$ python3 server.py -p portn°
 ```
El parámetro -p sirve para indicar por la terminal, en qué puerto se quiere atender el servicio
Una vez landazo el servidor podemos conectar clientes lanzandolos desde otras terminales de la siguiente manera:
 ```sh
$ source bin/activate
(directorio) ordenador@xx:path_directorio$ python3 client.py -a direcciónIp -p puerto
 ```
 Una vez lanzado los clientes usted verá que el servidor recibe las conexiones y queda pendiente para aceptar las solitudes que los clientes envíen por línea de comandos
