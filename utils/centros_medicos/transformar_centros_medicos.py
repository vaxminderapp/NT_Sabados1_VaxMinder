import random
import pandas as pd
from utils.centros_medicos.simular_centros_medicos import simular_centros_medicos


def transformar_centros_medicos(centros):
    tipos_invalidos = ["dispensario", "farmacia", ""]
    transformados = []

    for centro in centros:
        item = centro.copy()
        p = random.random()

        if p < 0.15:
            item["id_centro"] = random.choice([None, -1, 0])
        elif p < 0.30:
            item["nombre_centro"] = random.choice(["", None, "   "])
        elif p < 0.45:
            item["tipo_centro"] = random.choice(tipos_invalidos)
        elif p < 0.60:
            item["telefono"] = random.choice(["abc", "1", None])
        elif p < 0.75:
            item["direccion"] = None
            item["ciudad"] = None
        else:
            item["nombre_centro"] = "  " + item.get("nombre_centro", "") + "  "

        transformados.append(item)
    return transformados


def consultar_centros_medicos(df):
    print("\n--- Consultas centros medicos ---")
    print(f"  Hospitales: {len(df[df['tipo_centro'] == 'Hospital'])}")
    print(f"  Clinicas: {len(df[df['tipo_centro'] == 'Clinica'])}")
    print(f"  Centros de salud: {len(df[df['tipo_centro'] == 'Centro de salud'])}")
