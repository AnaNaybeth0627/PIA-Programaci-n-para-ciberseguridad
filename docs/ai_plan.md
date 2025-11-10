# Plan de Implementación de IA - Monitoreo de Procesos Sospechosos

## 1. Propósito de la IA en el Proyecto
Mejorar la detección de procesos maliciosos mediante aprendizaje automático, superando las reglas estáticas y adaptándose a nuevos patrones de amenazas.

## 2. Punto de Integración en el Flujo
**Módulo:** Tarea 3 - Detección de Procesos Sospechosos
**Ubicación:** Después de la recolección de métricas, antes de la generación de alertas

## 3. Tipo de Modelo/API
**Modelo:** Random Forest (scikit-learn)
**Alternativa:** Regresión Logística para explicabilidad
**Entrenamiento:** Supervisado con datos sintéticos

## 4. Características de Entrada
```json
{
  "cpu_percent": 85.5,
  "memory_mb": 256.0,
  "num_threads": 8,
  "user_type": "system",
  "process_name_score": 0.7,
  "parent_process": "explorer.exe"
}

