Este script realiza el análisis técnico del estado del disco.
Sus funciones principales incluyen:
Calcular el espacio total, usado y libre del sistema utilizando librerías estándar de Python (os, shutil, json, datetime).
Comparar los resultados con un registro previo estado_disco_anterior.json para detectar aumentos anómalos.
Generar alertas si el incremento supera el umbral definido en la configuración.
Exportar los resultados en un archivo estructurado salida_estado_disco.json.