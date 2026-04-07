from datetime import datetime, timedelta
import random


lotesVacuna = [
    "lot-2024-a1", "lot-2024-b2", "lot-2024-c3", "lot-2024-d4",
    "lot-2025-a1", "lot-2025-b2", "lot-2025-c3", "lot-2025-d4",
    "lot-2026-a1", "lot-2026-b2",
]

observaciones = [
    "paciente tolero bien la vacuna",
    "sin reacciones adversas inmediatas",
    "leve enrojecimiento en zona de aplicacion",
    "paciente presento fiebre leve post-aplicacion",
    "aplicacion sin inconvenientes",
    "se recomienda hidratacion posterior",
    "paciente nervioso, aplicacion exitosa",
    "sin observaciones relevantes",
    None,
    None,
]

fechaInicio = datetime(2024, 1, 1)
fechaFin = datetime(2026, 4, 1)


def _fechaAleatoria(inicio, fin):
    delta = fin - inicio
    return inicio + timedelta(days=random.randint(0, delta.days))


def _calcularProximaDosis(fechaAplicacion, intervaloDias, numeroDosis, dosisRequeridas):
    if numeroDosis >= dosisRequeridas or intervaloDias == 0:
        return None
    return fechaAplicacion + timedelta(days=intervaloDias)


def simularRegistroVacunacion(numeroRegistros, idsUsuarios, vacunasCatalogo, idsCentrosMedicos):
    """
    Simula datos para la tabla registro_vacunacion.

    Args:
        numeroRegistros (int): cantidad de registros a simular.
        idsUsuarios (list): lista de ids de usuarios existentes.
        vacunasCatalogo (list): lista de vacunas del catalogo con sus atributos.
        idsCentrosMedicos (list): lista de ids de centros medicos existentes.

    Returns:
        list: lista de diccionarios con datos de registros de vacunacion.
    """
    registros = []

    for idx in range(1, numeroRegistros + 1):
        vacuna = random.choice(vacunasCatalogo)
        numeroDosis = random.randint(1, vacuna["dosis_requeridas"])
        fechaAplicacion = _fechaAleatoria(fechaInicio, fechaFin)
        proximaDosis = _calcularProximaDosis(
            fechaAplicacion,
            vacuna["intervalo_dosis_dias"],
            numeroDosis,
            vacuna["dosis_requeridas"],
        )

        registro = {
            "idRegistro": idx,
            "idUsuario": random.choice(idsUsuarios),
            "idVacuna": vacuna["id_vacuna"],
            "fechaAplicacion": fechaAplicacion.date(),
            "numeroDosis": numeroDosis,
            "loteVacuna": random.choice(lotesVacuna),
            "idCentroMedico": random.choice(idsCentrosMedicos),
            "observaciones": random.choice(observaciones),
            "proximaDosisfecha": proximaDosis.date() if proximaDosis else None,
        }
        registros.append(registro)

    return registros