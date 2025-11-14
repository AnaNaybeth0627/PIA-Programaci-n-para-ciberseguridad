Entregable 5 - Tarea 2: Detección de Intentos Fallidos de Acceso
Descripción Específica:
Implementación de un sistema en Python que analiza archivos de logs sintéticos para identificar intentos fallidos de acceso al sistema y registrar eventos sospechosos.

##Características Analizadas:

Número de intentos fallidos por IP

Patrón de múltiples fallos consecutivos (3 o más)

Usuario afectado por los intentos fallidos

##Archivos de Salida Generados:
### `output_tarea2.json`

[
  {
    "timestamp": "2025-11-05T03:21:15",
    "source_ip": "192.168.1.12",
    "event": "multiple_failed_logins",
    "severity": "medium",
    "user": "root",
    "failed_attempts": 3,
    "tarea": "Tarea2_Deteccion_Intentos"
  },
  {
    "timestamp": "2025-11-05T03:23:06",
    "source_ip": "192.168.1.15",
    "event": "multiple_failed_logins",
    "severity": "medium",
    "user": "user1",
    "failed_attempts": 2,
    "tarea": "Tarea2_Deteccion_Intentos"
  }
]


##Reporte Resumido Generado:
### `reporte_tarea2.md`

Total de intentos fallidos: 7

IP con más intentos: 192.168.1.12

Eventos sospechosos detectados: 2
