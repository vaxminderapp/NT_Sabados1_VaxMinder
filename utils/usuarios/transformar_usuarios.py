import random
import pandas as pd
from utils.usuarios.simular_usuarios import simular_usuarios


def transformar_usuarios(usuarios):
    tipos_sangre_invalidos = ["Z+", "XX", "", None]
    transformados = []

    for usuario in usuarios:
        item = usuario.copy()
        # Solo 40% de usuarios reciben un error, el resto pasa limpio
        if random.random() > 0.40:
            transformados.append(item)
            continue

        p = random.random()
        if p < 0.17:
            item["id_usuario"] = random.choice([None, -1, 0])
        elif p < 0.34:
            item["nombre"] = random.choice(["", None])
            item["apellido"] = random.choice(["", None])
        elif p < 0.51:
            item["email"] = random.choice(["sinArroba.com", "@sinusuario.com", ""])
        elif p < 0.68:
            item["tipo_sangre"] = random.choice(tipos_sangre_invalidos)
        elif p < 0.85:
            item["fecha_nacimiento"] = None
            item["fecha_registro"] = None
        else:
            item["telefono"] = random.choice(["abc123", "1", None])

        transformados.append(item)
    return transformados


def consultar_usuarios(df):
    print("\n--- Consultas usuarios ---")
    print(f"  Total usuarios: {len(df)}")
    for tipo, cnt in df["tipo_sangre"].value_counts().items():
        print(f"  Tipo {tipo}: {cnt}")
