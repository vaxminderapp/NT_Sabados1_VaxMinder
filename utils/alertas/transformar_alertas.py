import random

from simular_alertas import simular_alertas


def transformar_alertas(alertas):
    alertas_transformadas = []

    for alerta in alertas:
        # Copia el registro para no modificar el original
        alerta_transformada = alerta.copy()

        # Inyectando errores controlados
        probabilidadError = random.random()
        if probabilidadError < 0.1:
            # ID y usuario inválidos
            alerta_transformada["id_alerta"] = random.choice([None, -1, 0])
            alerta_transformada["id_usuario"] = random.choice([None, -1, 0])
        elif probabilidadError < 0.25:
            # Fechas nulas
            alerta_transformada["fecha_alerta"] = None
            alerta_transformada["fecha_envio"] = None
        elif probabilidadError < 0.4:
            # Tipo y estado inválidos
            alerta_transformada["tipo_alerta"] = random.choice(["urgente", "critica", ""])
            alerta_transformada["estado"] = random.choice(["procesado", "archivado", ""])
        elif probabilidadError < 0.6:
            # Mensaje vacío o incoherente
            alerta_transformada["mensaje"] = random.choice(["", "   ", "N/A", None])
        elif probabilidadError < 0.8:
            # id_registro negativo o cero
            alerta_transformada["id_registro"] = random.choice([-5, 0, -999])
        else:
            # Estado pendiente con fecha_envio asignada (inconsistencia)
            alerta_transformada["estado"] = "pendiente"
            alerta_transformada["fecha_envio"] = "2026-02-01 08:00:00"

        alertas_transformadas.append(alerta_transformada)

    return alertas_transformadas


if __name__ == "__main__":
    alertas_simuladas = simular_alertas(5)
    print("Alertas simuladas:")
    print(alertas_simuladas)

    alertas_transformadas = transformar_alertas(alertas_simuladas)
    print("\nAlertas transformadas (con errores inyectados):")
    print(alertas_transformadas)
