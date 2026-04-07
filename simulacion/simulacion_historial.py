from datetime import datetime, timedelta
import random


prefijosArchivo = [
    "carnet_vacunacion",
    "historial_vacunas",
    "certificado_vacunacion",
    "reporte_vacunas",
    "registro_vacunacion",
]

rutaBase = "/storage/pdfs/usuarios/"

fechaInicio = datetime(2024, 1, 1)
fechaFin = datetime(2026, 4, 1)


def _fechaAleatoria(inicio, fin):
    delta = fin - inicio
    return inicio + timedelta(days=random.randint(0, delta.days))


def _generarNombreArchivo(idUsuario, fecha):
    prefijo = random.choice(prefijosArchivo)
    timestamp = fecha.strftime("%Y%m%d_%H%M%S")
    return f"{prefijo}_{idUsuario}_{timestamp}.pdf"


def _generarRutaArchivo(idUsuario, nombreArchivo):
    return f"{rutaBase}{idUsuario}/{nombreArchivo}"


def simularHistorialPdf(numeroRegistros, idsUsuarios):
    """
    Simula datos para la tabla historial_pdf.

    Args:
        numeroRegistros (int): cantidad de registros a simular.
        idsUsuarios (list): lista de ids de usuarios existentes.

    Returns:
        list: lista de diccionarios con datos del historial de pdfs generados.
    """
    registros = []

    for idx in range(1, numeroRegistros + 1):
        idUsuario = random.choice(idsUsuarios)
        fechaGeneracion = _fechaAleatoria(fechaInicio, fechaFin)
        nombreArchivo = _generarNombreArchivo(idUsuario, fechaGeneracion)
        rutaArchivo = _generarRutaArchivo(idUsuario, nombreArchivo)

        registro = {
            "idHistorial": idx,
            "idUsuario": idUsuario,
            "fechaGeneracion": fechaGeneracion,
            "nombreArchivo": nombreArchivo,
            "rutaArchivo": rutaArchivo,
        }
        registros.append(registro)

    return registros