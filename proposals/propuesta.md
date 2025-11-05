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
# Tarea 3: Detección de procesos sospechosos en ejecución

Propósito: Monitorear y identificar procesos del sistema que presenten características sospechosas o maliciosas basándose en patrones de comportamiento y consumo de recursos.

Función, rol o área de la ciberseguridad relacionada: EDR (Endpoint Detection and Response) - Análisis de comportamiento de procesos. 

Entradas esperadas:
- Lista de procesos en ejecución del sistema
- Patrones de procesos sospechosos (ej: nombres similares a system32, alto consumo de CPU, múltiples instancias)
- Umbrales de detección configurables


Salidas esperadas: Archivo procesos_sospechosos.json con detalles de cada proceso detectado:

{ 
  "pid": 1234,
  "nombre": "svchost.exe",
  "consumo_cpu": 85.5,
  "usuario": "system",
  "riesgo": "medio",
  "razon": "Alto consumo de recursos"
}

Reporte en tiempo real en consola de procesos activos monitoreados

Descripción del procedimiento: El sistema obtendrá periódicamente la lista de procesos en ejecución, analizará su comportamiento (consumo de recursos, nombre, usuario) y comparará contra patrones predefinidos para identificar actividades sospechosas. 

Complejidad técnica: Obtención de métricas de procesos en tiempo real, Análisis de patrones y comportamientos, Gestión de intervalos de monitoreo, Clasificación de niveles de riesgo. 

Controles éticos: Solo monitoreo de procesos en ambiente controlado con datos sintéticos, sin interrumpir procesos del sistema real.

Dependencias: Python 3.10+, librerías: psutil, time, json

-----------------------


-----------------------
# Tarea 4 Análisis de espacio en disco y almacenamiento:

Propósito: Monitorear el uso de espacio en disco para detectar crecimientos anómalos o comportamientos inusuales que puedan indicar generación de archivos sospechosos, copias no autorizadas que afecten la seguridad y el rendimiento del sistema.

Función, rol o área de la ciberseguridad relacionada: Blue team - Detección tempana de incidentes de archivos maliciosos o logs excesivos.

Entradas esperadas:
-Directorio base del sistema (/home/usuario/).
-Estado previo del espacio ocupado para realizar la comparación (estado_disco_anterior.json).
-Parametro de umbral configurable es el porcentaje de uso o incremento maximo permitido.

Salidas esperadas:
-Archivo de reporte reporte_espacio_disco.json.
-Archivo que resume reporte_disco.md con alertas clave para el equipo de seguridad.

Ejemplo:
Uso total del disco: 45.6 GB / 50 GB (91%)
Incremento detectado: +5.2 GB desde el ultimo registro
Carpeta con mayor crecimiento: /home/usuario/descargas/
Estado general: ALERTA

Descripción del procedimiento:El script se inicia obteniendo el estado actual del espacio total y disponible del disco. Luego lee el estado_disco_anterior.json. Analiza el crecimiento absoluto y relativo de cada directorio, comparando los resultados del estado actual contra el estado anterior. Si el aumento de espacio ocupado supera el umbral establecido, el script genera una alerta detallada. Este proceso de comparación de estados y el registro de la alerta se guardan inmediatamente en los archivos de salida JSON.También se realiza una actualización del archivo estado_disco_anterior.json para la siguiente ejecución.

Complejidad técnica:Lectura y análisis del sistema de archivos, comparación de estados previos de almacenamiento, y automatización del monitoreo con Python utilizando librerías estándar para recopilar métricas del disco y generar reportes estructurados.

Controles éticos:El monitoreo debe realizarse únicamente en entornos controlados y sobre directorios autorizados, como entornos de laboratorio o carpetas de uso general.

Dependencias:
-Python 3.10+
-Librerías estándar: os, json, time, shutil.
-Permisos de lectura sobre los directorios a analizar.
-Archivo de configuración con los umbrales de alerta.

-----------------------

### Roles del equipo: 

Ana Naybeth Medina Perez| Lectura y registro de archivos criticos

Angel Gabriel Cruz Velazquez| Detección de intentos de acceso sospechosos en logs

Karyme Gisel González Aguillón| Detección de procesos sospechosos en ejecución

Jesus Alejandro Ramirez Baltazar | Análisis de espacio en disco y almacenamiento

### Declaracion Etica y Legal: 

Este proyecto se llevará a cabo respetando la confidencialidad y privacidad de la información del sistema, garantizando que no se modifiquen los archivos del sistema durante el proceso de supervisión.


-----------------------
