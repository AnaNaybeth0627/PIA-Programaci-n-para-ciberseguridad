import re
import json
from datetime import datetime
import os

# ==========================
# Función para generar logs sintéticos
# ==========================
def generar_logs_automaticos(ruta_logs):
    contenido = """[2025-11-05 03:21:15] login failed for user 'root' from 192.168.1.12
[2025-11-05 03:21:16] login failed for user 'root' from 192.168.1.12
[2025-11-05 03:21:17] login failed for user 'root' from 192.168.1.12
[2025-11-05 03:22:01] login success for user 'admin' from 10.0.0.4
[2025-11-05 03:23:05] login failed for user 'user1' from 192.168.1.15
[2025-11-05 03:23:06] login failed for user 'user1' from 192.168.1.15
[2025-11-05 03:30:10] login failed for user 'guest' from 172.16.0.5
"""
    with open(ruta_logs, "w", encoding="utf-8") as file:
        file.write(contenido)
    print(f"[OK] Archivo de logs generado en: {ruta_logs}")

# ==========================
# Función para registrar logs internos de la tarea
# ==========================
def log_event(mensaje, nivel="INFO"):
    evento = {
        "timestamp": datetime.now().isoformat(),
        "level": nivel,
        "message": mensaje
    }
    with open("logs_tarea2.jsonl", "a") as f:
        f.write(json.dumps(evento) + "\n")

# ==========================
# Función para analizar logs y detectar eventos sospechosos
# ==========================
def analizar_logs(ruta_logs):
    if not os.path.exists(ruta_logs):
        log_event(f"Archivo no encontrado: {ruta_logs}", "ERROR")
        return [], {}

    patron = re.compile(
        r"\[(.*?)\]\s+login\s+(failed|success)\s+for user '(.+?)'\s+from\s+(\d+\.\d+\.\d+\.\d+)"
    )

    intentos_por_ip = {}
    eventos_sospechosos = []

    with open(ruta_logs, "r") as archivo:
        for linea in archivo:
            m = patron.search(linea)
            if not m:
                continue

            timestamp, resultado, usuario, ip = m.groups()

            if resultado == "failed":
                intentos_por_ip[ip] = intentos_por_ip.get(ip, 0) + 1

                if intentos_por_ip[ip] == 3:  # Si hay 3 intentos fallidos, se marca como sospechoso
                    evento = {
                        "timestamp": timestamp,
                        "source_ip": ip,
                        "event": "multiple_failed_logins",
                        "severity": "medium",
                        "user": usuario,
                        "failed_attempts": intentos_por_ip[ip]
                    }
                    eventos_sospechosos.append(evento)
                    log_event(f"Intentos sospechosos detectados en IP {ip}", "WARNING")

    return eventos_sospechosos, intentos_por_ip

# ==========================
# Función para guardar resultados
# ==========================
def guardar_resultados(eventos, resumen, archivo_jsonl="output_tarea2.jsonl", reporte_md="reporte_tarea2.md"):
    # Guardar JSONL
    with open(archivo_jsonl, "w") as f:
        for e in eventos:
            f.write(json.dumps(e) + "\n")

    # Guardar reporte Markdown
    with open(reporte_md, "w") as f:
        f.write("# Reporte Tarea 2: Intentos de acceso sospechosos\n\n")
        f.write(f"- Total de intentos fallidos: {resumen['total_intentos']}\n")
        f.write(f"- IP con más intentos: {resumen['ip_mas_intentos']}\n")
        f.write(f"- Eventos sospechosos detectados: {resumen['eventos_sospechosos']}\n")

    log_event("Resultados guardados correctamente.")

# ==========================
# Función principal que ejecuta la tarea completa
# ==========================
def ejecutar_tarea2():
    ruta_logs = "logs_prueba_tarea2.txt"

    # Generar archivo de logs sintético
    generar_logs_automaticos(ruta_logs)

    # Analizar los logs
    eventos, intentos_por_ip = analizar_logs(ruta_logs)

    # Crear resumen
    resumen = {
        "total_intentos": sum(intentos_por_ip.values()),
        "ip_mas_intentos": max(intentos_por_ip, key=intentos_por_ip.get) if intentos_por_ip else "N/A",
        "eventos_sospechosos": len(eventos)
    }

    # Guardar resultados en JSONL y Markdown
    guardar_resultados(eventos, resumen)

    print("Tarea 2 completada.")
    log_event("Tarea 2 ejecutada exitosamente.")

# ==========================
# Ejecutar si es el archivo principal
# ==========================
if __name__ == "__main__":
    ejecutar_tarea2()
