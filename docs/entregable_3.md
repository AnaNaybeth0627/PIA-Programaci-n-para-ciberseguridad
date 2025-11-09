En esta tercera entrega se realizo la tarea 4 que implementa un sistema híbrido desarrollado en PowerShell y Python que realiza el monitoreo del espacio en disco del sistema.

El componente principal (analisis_espacio_disco.psm1) actúa como módulo de orquestación en PowerShell, la cual es el encargado de leer la configuración desde un archivo JSON (prompt_V1.json), ejecutar el script Python asociado y centralizar los resultados.
El script secundario (analisis_espacio_disco.py) realiza el cálculo del espacio total, usado y libre, compara el estado actual con un registro previo (estado_disco_anterior.json) y determina si existe un incremento significativo de uso que pueda representar actividad inusual o maliciosa.

Durante la ejecución, se generan registros estructurados en formato JSON Lines (salida_estado_disco.json), que contienen campos clave:

timestamp: fecha y hora del evento

run_id: identificador de ejecución del análisis

module: nombre del módulo (analisis_espacio_disco)

level: nivel del evento (INFO, ALERTA, ERROR)

event: tipo de evento registrado (análisis, error, alerta)

details: información técnica (ruta monitoreada, uso actual, incremento detectado, umbral aplicado)

El script PowerShell (run_pipeline.ps1) automatiza el flujo completo del análisis, asegurando que la configuración y las rutas se carguen correctamente, ejecutando el módulo de Python y almacenando los resultados dentro de la carpeta /examples/.

Este diseño cumple con los requisitos de automatización, registro estructurado, modularidad y uso de múltiples lenguajes.