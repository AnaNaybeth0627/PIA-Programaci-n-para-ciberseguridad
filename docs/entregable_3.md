Como primer parte de es este entregable se realizo la tarea adicional conectada con la tarea uno, esta tarea se encarga
de la creacion de un grafico mostrando el tipo de cambios que ocurren en las fechas registradas, su funcion consiste
en realizar primero la lectura del archivo .txt generado por la tarea 1 qeu lleva por nombre reporte_de_cambios.txt
y y crea un gráfico de barras apiladas con los tipos de cambios por fecha. Tambien permite registrar eventos en un 
archivo JSON (logs.jsonl) usando la función log_eventos. Cada registro incluye:

- timestamp: fecha y hora del evento.

- evento: descripción del evento.

- detalles: información adicional, como la ruta del archivo.

Estos eventos registran la existencia del archivo reporte_de_cambios.txt finalmente los registros JSON se crean en la 
carpeta donde se ejecuta el script.

La Tarea 4 esta centrada en el análisis de espacio en disco y almacenamiento del sistema.
Esta tarea tiene como objetivo monitorear el uso de almacenamiento en una ruta específica y detectar incrementos significativos que puedan representar un riesgo o un comportamiento anómalo dentro del sistema.

El archivo prompt_V1.json especifica los parámetros como la ruta del directorio a analizar, el umbral de alerta y los nombres de los archivos de salida que posteriormente, ejecuta el script en Python con los argumentos necesarios para realizar el análisis y genera los resultados correspondientes.

El archivo analisis_espacio_disco.py es el responsable de obtener el uso actual del disco, comparar los valores con un estado previo almacenado en un archivo JSON y calcular el incremento en el uso de espacio.

Luego se genera el archivo Salida_estado_disco.jsonl la cual este registro incluye los siguientes campos:
-timestamp: fecha y hora del evento.
-run_id: identificador único de ejecución.
-module: nombre del módulo o script ejecutado.
-level: nivel del evento (INFO, ALERTA, BIEN, ERROR).
-event: tipo de análisis realizado.
-details: información detallada del análisis, incluyendo ruta monitoreada, uso actual, incremento detectado y umbral aplicado.

Por ultimo el script run_pipeline.ps1 permite ejecutar toda la tarea con un solo comando.

(segunda parte)
