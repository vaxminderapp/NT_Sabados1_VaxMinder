import random
import pandas as pd

from utils.centros_medicos.simular_centros_medicos import simular_centros_medicos


def transformar_centros_medicos(centros):
    centros_transformados = []

    for centro in centros:
        # Copia el registro para no modificar el original
        centro_transformado = centro.copy()

        # Inyectando errores controlados
        probabilidadError = random.random()
        if probabilidadError < 0.1:
            # ID inválido y nombre vacío
            centro_transformado["id_centro"] = random.choice([None, -1, 0])
            centro_transformado["nombre_centro"] = random.choice(["", None, "   "])
        elif probabilidadError < 0.25:
            # Dirección y ciudad nulas
            centro_transformado["direccion"] = None
            centro_transformado["ciudad"] = None
        elif probabilidadError < 0.4:
            # Teléfono con formato inválido
            centro_transformado["telefono"] = random.choice(["abc-xyz", "123", "", None])
        elif probabilidadError < 0.6:
            # Tipo de centro inválido
            centro_transformado["tipo_centro"] = random.choice(["dispensario", "farmacia", "", None])
        elif probabilidadError < 0.8:
            # Nombre con espacios extra o caracteres raros
            nombre = centro_transformado.get("nombre_centro", "")
            centro_transformado["nombre_centro"] = "  " + nombre + "  "
        else:
            # Ciudad en mayúsculas inconsistentes
            ciudad = centro_transformado.get("ciudad", "")
            centro_transformado["ciudad"] = ciudad.upper() if ciudad else None

        centros_transformados.append(centro_transformado)

    return centros_transformados


def consultar_centros_medicos(df: pd.DataFrame) -> None:
    print("\n========== CONSULTAS: CENTROS MÉDICOS ==========")

    hospitales = df.query("tipo_centro == 'Hospital'")
    print(f"\n[1] Solo hospitales ({len(hospitales)} registros):")
    print(hospitales[['id_centro', 'nombre_centro', 'ciudad', 'tipo_centro']].to_string())

    no_hospitales = df.query("tipo_centro != 'Hospital'")
    print(f"\n[2] Clínicas y centros de salud ({len(no_hospitales)} registros):")
    print(no_hospitales[['id_centro', 'nombre_centro', 'ciudad', 'tipo_centro']].to_string())

    primeros = df.query("id_centro <= 15")
    print(f"\n[3] Centros con ID menor o igual a 15 ({len(primeros)} registros):")
    print(primeros[['id_centro', 'nombre_centro', 'tipo_centro']].to_string())


if __name__ == "__main__":
    centros_simulados = simular_centros_medicos(5)
    print("Centros simulados:")
    print(centros_simulados)

    centros_transformados = transformar_centros_medicos(centros_simulados)
    print("\nCentros transformados (con errores inyectados):")
    print(centros_transformados)
