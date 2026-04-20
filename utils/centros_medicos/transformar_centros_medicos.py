import random

from simular_centros_medicos import simular_centros_medicos


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


if __name__ == "__main__":
    centros_simulados = simular_centros_medicos(5)
    print("Centros simulados:")
    print(centros_simulados)

    centros_transformados = transformar_centros_medicos(centros_simulados)
    print("\nCentros transformados (con errores inyectados):")
    print(centros_transformados)
