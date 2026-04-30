import random
import pandas as pd
from utils.alertas.simular_alertas import simular_alertas


def transformar_alertas(alertas):
    tipos_invalidos  = ["urgente", "critica", ""]
    estados_invalidos = ["procesado", "archivado", ""]
    transformadas = []

    for alerta in alertas:
        item = alerta.copy()
        # Solo 40% reciben un error
        if random.random() > 0.40:
            transformadas.append(item)
            continue

        p = random.random()
        if p < 0.20:
            item["id_alerta"]  = random.choice([None, -1, 0])
        elif p < 0.40:
            item["id_registro"] = random.choice([None, -5, -999])
        elif p < 0.55:
            item["fecha_alerta"] = None
        elif p < 0.70:
            item["tipo_alerta"] = random.choice(tipos_invalidos)
            item["estado"]      = random.choice(estados_invalidos)
        elif p < 0.85:
            item["mensaje"] = random.choice(["", "N/A", None])
        else:
            # inconsistencia: pendiente con fecha_envio asignada
            item["estado"]      = "pendiente"
            item["fecha_envio"] = "2026-02-01"

        transformadas.append(item)
    return transformadas


def consultar_alertas(df):
    print("\n--- Consultas alertas ---")
    print(f"  Pendientes : {len(df[df['estado'] == 'pendiente'])}")
    print(f"  Enviadas   : {len(df[df['estado'] == 'enviada'])}")
    print(f"  Leidas     : {len(df[df['estado'] == 'leida'])}")
    print(f"  Descartadas: {len(df[df['estado'] == 'descartada'])}")

