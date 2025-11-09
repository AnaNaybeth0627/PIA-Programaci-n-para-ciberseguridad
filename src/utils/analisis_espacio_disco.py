import os
import json
import argparse
import shutil
import sys 
from datetime import datetime

def obtener_uso_disco(path):
    total, usado, libre = shutil.disk_usage(path)
    return {"total_gb": round(total / (1024**3), 2),
            "usado_gb": round(usado / (1024**3), 2),
            "libre_gb": round(libre / (1024**3), 2)}

def registrar_evento(log_file, evento):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(evento) + "\n")

def main():
    parser = argparse.ArgumentParser(description="Análisis de espacio en disco")
    parser.add_argument("--path", required=True, help="Ruta base a analizar")
    parser.add_argument("--prev", required=False, help="Archivo con estado previo")
    parser.add_argument("--threshold", type=float, default=10.0, help="Umbral de alerta en %")
    parser.add_argument("--output", required=True, help="Archivo JSONL de salida")
    args = parser.parse_args()

    # 1. Obtene el uso actual del disco
    try:
        current_usage = obtener_uso_disco(args.path)
    except FileNotFoundError:
        print(f"ERROR: Ruta no encontrada {args.path}", file=sys.stderr)
        sys.exit(1)
    
    # 2. Carga el uso previo del disco
    prev_usage = None
    if args.prev and os.path.exists(args.prev):
        try:
            with open(args.prev, "r", encoding="utf-8") as f:
                prev_usage = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass 

    #  3. Analizar Incremento de Uso 
    incremento_gb = 0
    estado = "INFO" 

    if prev_usage and 'usado_gb' in prev_usage:
        incremento_gb = current_usage["usado_gb"] - prev_usage["usado_gb"]
        
        if incremento_gb > 0 and (incremento_gb / prev_usage["usado_gb"]) * 100 > args.threshold:
            estado = "ALERTA"
        elif incremento_gb > 0:
            estado = "INFO"
        else:
            estado = "BIEN" 
            
    # 4. Registrar Evento de Análisis
    evento = {
        "timestamp": datetime.now().isoformat(),
        "run_id": os.getpid(),
        "module": "analisis_espacio_disco",
        "level": estado,
        "event": "analisis_de_comportamiento",
        "details": {
            "path": args.path,
            "uso_actual_gb": current_usage["usado_gb"],
            "incremento_gb": round(incremento_gb, 2),
            "umbral_aplicado": f"{args.threshold}%",
            "mensaje": f"Crecimiento de {round(incremento_gb, 2)} GB detectado."
        }
    }
    registrar_evento(args.output, evento)

    # 5. Guarda el nuevo estado 
    if args.prev:
        try:
            with open(args.prev, "w", encoding="utf-8") as f:
                json.dump(current_usage, f, indent=4)
        except Exception as e:
            registrar_evento(args.output, {"timestamp": datetime.now().isoformat(), "level": "ERROR", "module": "disk_analyzer", "event": "Error_Guardar_Estado", "details": str(e)})
            sys.exit(2)

if __name__ == "__main__":
    main()