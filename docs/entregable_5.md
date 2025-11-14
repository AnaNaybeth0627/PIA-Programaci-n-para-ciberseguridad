# Entregable 5 - Tarea 2: Detección de Intentos de Acceso Sospechosos

## Descripción Específica
Implementación completa del sistema de análisis de logs sintéticos para identificar intentos fallidos de acceso al sistema. El script detecta patrones de múltiples intentos fallidos desde la misma IP y registra eventos sospechosos.

## Características Analizadas
1. **Número de intentos fallidos** por IP (>=3 fallidos genera alerta)
2. **IP origen** del intento de acceso
3. **Usuario** intentando acceder
4. **Timestamp** del evento
5. **Severidad** del evento (ej. medium)

## Archivos de Salida Generados

### `output_tarea2.json`
```json
[
  {
    "timestamp": "2025-11-05T03:21:17",
    "source_ip": "192.168.1.12",
    "user": "root",
    "event": "multiple_failed_logins",
    "severity": "medium",
    "failed_attempts": 3,
    "tarea": "Tarea2_Deteccion_Intentos"
  },
  {
    "timestamp": "2025-11-05T03:23:06",
    "source_ip": "192.168.1.15",
    "user": "user1",
    "event": "multiple_failed_logins",
    "severity": "medium",
    "failed_attempts": 3,
    "tarea": "Tarea2_Deteccion_Intentos"
  }
]
