import random
from utils.historialPdf.simular_historial import simularHistorialPdf


def transformar_historial(historial):
    transformado = []
    for item in historial:
        r = item.copy()
        if random.random() > 0.40:
            transformado.append(r)
            continue
        p = random.random()
        if p < 0.25:
            r["idHistorial"] = random.choice([None, 0, -1])
            r["idUsuario"]   = random.choice([None, 0, -5])
        elif p < 0.50:
            r["fechaGeneracion"] = None
        elif p < 0.75:
            r["nombreArchivo"] = random.choice(["", None, "archivo.txt"])
        else:
            r["rutaArchivo"] = random.choice(["", None, "/ruta/invalida"])
        transformado.append(r)
    return transformado
