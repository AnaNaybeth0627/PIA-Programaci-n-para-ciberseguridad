En esta segunda entrega se realizo la finalizacion del script de la tarea 1 encargado de leer y registrar los cambios en 
los archivos del usuario.

La ejecucion de este script es bastante sencilla se llamara desde el menu correspondiente presionando la tecla numerica que le 
indique el menu, se realizara automaticamente la lectura de todos los archivos pertenecientes en "C:\Users\usuario" que esten
sufriendo un cambio en el sistema, esto se realizara en tiempo real, por lo que el script indica al inicio de su ejecucion que se
presione la tecla enter en caso de querer detener el proceso, una vez presionada la tecla se mostrara en pantalla todos los
eventos ocurridos, incluyendo:

  -El tipo de evento(Created, Changed, Deleted, Renamed)
  -La hora y fecha en la que se realizo
  -La ruta del archivo afectado

Finalmente se generaran registros de todos los eventos en formato .txt y JSON. Cada evento registrado incluye información clave
en formato JSON line, cumpliendo con los estándares de logging del proyecto:

  -timestamp: fecha y hora del evento
  -run_id: identificador único de ejecución
  -module: nombre del módulo (FileWatcher)
  -level: nivel de registro (INFO)
  -event: tipo de evento (Created, Changed, Deleted, Renamed)
  -details: ruta completa del archivo afectado

Este diseño garantiza evidencia reproducible, con historial completo de cambios, y permite su integración directa con el flujo
del proyecto y el menú principal.
