# Readme
En este archivo se explicará el uso básico del sistema. Se debe tener en cuenta cómo se deben ejecutar los archivos cliente y servidor. *Información presente en install*

# Inserción de un nuevo ticket
Para la inserción de un nuevo ticket, cuando aparezcan visibles todas las opciones disponibles para ejecutar, se debe ingresar por consola de la terminal:
```sh
$ --insert
```
O bien, su versión acortada para el comando, **-i**.
Una vez hecho esto, el servidor le devolverá los comandos disponibles para la inserción de un nuevo ticket. Entre las nuevas argumentos para insertar el nuevo ticket encontramos:
- **title** con su comando **-t**
- **author** con su comando **-a**
- **description** con su comando **-d**

Ejemplo de inserción de un Nuevo Ticket.
```sh
$ -tTitulo Nuevo -aLorem Ipsum -dUna nueva descripción
```
Si la creación del ticket fue satisfactoria, será notificada al cliente.

# Listar un Ticket
Para listar un conjunto de tickets, cuando aparecen las distintas alternativas para los comandos, se debe ingresar:
```sh
$ --list
```
O bien, su versión acortada para el comando, **-l**
La funcionalidad de listar tickets cuenta con 2 cursos alternativos internos, es decir, **listar todos los tickets** o **listar tickets por filtro**, ambas de estas funcionalidades cuentan con *paginación*, con el comando *-p*.
**Ejemplo de listado de todos los tickets.**
```sh
$ -v -p1
```
Esto listará todos los tickets disponibles, en la página uno gracias a -v. Por defecto, si la página no es especificada, el sistema traerá siempre la *número 1*
**Ejemplo de listado utilizando filtro**
Para el listado de tickets a parte del comando *-p*, para el seleccionado de páginas, existen otros nuevos, que pueden ser aplicados simultáneamente o no, según nuestras preferencias.
- **author** con su comando **-a**
- **date** con su comando **-d**
- **status** con su comando **-s**

```sh
$ -aLorem Ipsum -d19/05/2020 -sin process 
```
Cabe recalcar, que al utilizar el filtro, se deben tener en cuenta que la fecha debe estar en formato: *dd/MM/YYYY* mientras que los estados que puede tener un ticket son *in process*, *pending*, *solved*.
# Editar un Ticket
Para editar un ticket es necesario conocer el *Id* del ticket en cuestión, la edición es instantánea, asique es necesario pasar como argumentos los valores que se quieren modificar del mismo.
Los argumentos para editar son *Titulo -t*, *Estado -s*, *Descripción -d*
**Ejemplo del editado de un Ticket**
Supongamos que queremos editar el *Ticket 11*, la secuencia de ejecución sería:
```sh
$ --edit 'O tambien la versión corta -e' 
```
Una vez que ejecutamos el comando editar, pasamos los argumentos:
```sh
$ -i11 -tTitulo a buscar -sin process -dNueva,descripcion en texto. 
```
# Exportación de tickets.
Para exportar tickets, el uso es similar al de **Listar un ticket**, el mismo cuenta con la misma opción para filtrar los tickets, en este caso para exportarlos (*Los mismos son tambíen simultáneos*). También se cuenta con la paginación con *-p*

```sh
$ --export 'O la versión acotada -x' 
```
Luego, se puede decidir si exportar todos con **-v**, o filtrar por { **author** con su comando **-a** , **date** con su comando **-d**,  **status** con su comando **-s**}. (Se puede combinar con paginación)
```sh
$ -d19/05/2020 -p1
```
Lo cual exportará todos los tickets con esa fecha en la página 1. (*Paginacion es opcional*)

# Limpiar la terminal.
Si bien el limpiado de la terminal ocurre normalmente cuando se ejecuta un nuevo comando, en caso de que sea necesario, el sistema cuenta con el comando `--clear` / *version acotada -c*
# Salir del sistema
Para salir del sistema se tiene que ingresar el comando`--exit`



