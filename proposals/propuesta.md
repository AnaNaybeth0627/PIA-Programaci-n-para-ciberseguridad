# Titulo del proyecto: Monitoreo de seguridad en archivos del sistema



## Fichas Tecnicas

-----------------------
# Tarea 1 (Lectura y Registro de archivos criticos):

Propósito: Detectar y registrar cambios en archivos críticos del sistema ubicados en el directorio base y todas sus subcarpetas

Función, rol o área de la ciberseguridad relacionada: Blue Team-Deteccion de cambios en archivos criticos del sistema y del registro de eventos con fecha y hora.

Entradas esperadas: lectura de todos los archivos dentro del directorio base /home/usuario/ incluyendo las subcarpetas.
Archivo de estado previo por ejemplo (estado_anterior.json o estado_anterior.txt)

Salidas esperadas: informacion de cuando y que cambio ocurrio, con fecha y hora del evento.

ejemplo del archivo de registro .txt

[2025-11-05 15:30:22] Modificado: /home/usuario/documentos/ejemplo.txt

Detalles del cambio:
-linea 7 modificada: "Este es un ejemplo" → "Este no es un ejemplo"

[2025-11-05 15:31:05] Creado: /home/usuario/imagenes/ejemplo2.png
[2025-11-05 15:32:10] Eliminado: /home/usuario/scripts/ejemplo3.sh

Descripción del procedimiento: Se leen los archivos criticos y anota cualquier cambio detectado en un archivo de texto, indicando el archivo modificado con su fecha y hora del cambio.

Complejidad técnica: Lectura de archivos, comparar su estado actual con el archivo previo y registrar los cambios en un archivo txt. Tener un conocimiento en el manejo de rutas y recorre las subcarpetas del misimo directorio.

Controles éticos: Garantizar la confidencialidad de los archivos críticos al no modificar su contenido durante la lectura.

Dependencias: Sistema operativo con permisos adecuados y herramienta de registro para almacenar cambios.

-----------------------


-----------------------
# Tarea 2: Detección de intentos de acceso sospechosos en logs

Propósito:
El módulo busca detectar intentos de acceso no autorizados al sistema. Esto se logra mediante el análisis de archivos de registro (logs) para identificar patrones de intentos fallidos y accesos sospechosos.

Función, rol o área de la ciberseguridad relacionada:
SOC – Monitoreo y detección de intentos de acceso no autorizados en registros del sistema.

Entradas esperadas (formato y ejemplos):
Archivos de logs en formato .log o .txt, generados sintéticamente.
Contienen registros de autenticación con fecha, usuario, IP y resultado.

Ejemplo:

[2025-11-05 03:21:15] login failed for user 'root' from 192.168.1.12  
[2025-11-05 03:21:16] login failed for user 'root' from 192.168.1.12  
[2025-11-05 03:22:01] login success for user 'admin' from 10.0.0.4

Salidas esperadas (formato y ejemplos):
Archivo output_tarea2.jsonl con eventos sospechosos en formato JSON lines:

{"timestamp": "2025-11-05T03:21:15", "source_ip": "192.168.1.12", "event": "multiple_failed_logins", "severity": "medium"}

Reporte `reporte_tarea2.md` con resumen de hallazgos:  

- Total de intentos fallidos: **8**  
- IP con más intentos: **192.168.1.12**  
- Eventos sospechosos detectados: **2**

Descripción del procedimiento:
El sistema analiza los registros del sistema para identificar múltiples intentos fallidos de acceso desde una misma IP. Los eventos sospechosos se clasifican por severidad y se guardan en archivos estructurados y reportes legibles.

Complejidad técnica:
Procesamiento y parsing de texto, correlación de eventos, y automatización con Python utilizando librerías estándar.

Controles éticos:
Se emplean únicamente datos sintéticos; no se usan registros reales ni información sensible.

Dependencias:
Python 3.10+, librerías estándar (re, datetime, json, logging) y entorno local controlado.

-----------------------


-----------------------
# Tarea 3 (Titulo):

Función, rol o área de la ciberseguridad relacionada: 
Entradas esperadas:
Salidas esperadas:
Descripción del procedimiento:
Complejidad técnica:
Controles éticos:
Dependencias:

-----------------------


-----------------------
# Tarea 4 (Titulo):

Función, rol o área de la ciberseguridad relacionada: 
Entradas esperadas:
Salidas esperadas:
Descripción del procedimiento:
Complejidad técnica:
Controles éticos:
Dependencias:

-----------------------

### Roles del equipo: 

Ana Naybeth Medina Perez| Lectura y registro de archivos criticos

Angel Gabriel Cruz Velazquez| Detección de intentos de acceso sospechosos en logs

### Declaracion Etica y Legal: 

Este proyecto se llevará a cabo respetando la confidencialidad y privacidad de la información del sistema, garantizando que no se modifiquen los archivos del sistema durante el proceso de supervisión.


-----------------------
