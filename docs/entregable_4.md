# Entregable 4 - Tarea 3: Detección de Procesos Sospechosos con IA

## Descripción Específica
Implementación completa del sistema de detección de procesos sospechosos en ejecución utilizando inteligencia artificial (Random Forest) para identificar patrones maliciosos basados en comportamiento.

## Características Analizadas por la IA
1. **Uso de CPU** (>70% considerado sospechoso)
2. **Consumo de memoria** (>300MB alerta)
3. **Número de hilos** (>15 hilos sospechoso)
4. **Tipo de usuario** (System/Admin más riesgosos)
5. **Longitud del nombre** (Nombres largos sospechosos)
6. **Proceso padre** (Procesos hijos de cmd/powershell)

## Archivos de Salida Generados

### `resultados_tarea3.json`
```json
[
  {
    "pid": 1234,
    "nombre": "suspicious_process.exe",
    "usuario": "SYSTEM",
    "es_sospechoso": true,
    "confianza_ia": 0.892,
    "caracteristicas": {
      "cpu_percent": 85.2,
      "memory_mb": 356.7,
      "num_threads": 25,
      "tipo_usuario": "system",
      "longitud_nombre": 28
    },
    "timestamp": "2024-01-15T10:30:00",
    "tarea": "Tarea3_Deteccion_Procesos"
  }
]
