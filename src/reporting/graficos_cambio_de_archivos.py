import matplotlib.pyplot as plt
import pandas as pd
import os
import json
from datetime import datetime

ruta_archivo = os.path.expanduser("~/reporte_de_cambios.txt")


def log_eventos(evento, detalles=""):
    ent = {
        "timestamp": datetime.now().isoformat(),
        "evento": evento,
        "detalles": detalles
    }
    with open("logs.jsonl", "a") as f:
        f.write(json.dumps(ent) + "\n")

def grafica_cambios(ruta):
    fechas=[]
    cambios=[]
    archivos=[]

    ruta = os.path.expanduser("~/reporte_de_cambios.txt")
    with open(ruta, "r") as f:
        lineas = f.readlines()
        for linea in lineas:
            linea= linea.strip()
            if not linea:
                continue
            fecha, cambio, archivo=linea.split("  ", 2)
            fechas.append(fecha)
            cambios.append(cambio)
            archivos.append(archivo)

    dtf= pd.DataFrame({"fecha":fechas, "cambio":cambios, "archivo": archivos})
    cnt= dtf.groupby(["fecha", "cambio"]).size().unstack(fill_value=0)
    cnt.plot(kind="bar",stacked=True, figsize=(9,5), color={"Created": "#609C07","Renamed": "#FFEC21", "Changed": "#FD5D19", "Deleted": "#BB0000"} )

    plt.title("Cambios por tipo y fecha")
    plt.xlabel("Fecha")
    plt.ylabel("Cantidad de cambios")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

