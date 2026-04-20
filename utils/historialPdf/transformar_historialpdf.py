import random
from simular_historial import simularHistorialPdf


def transformar_historial(historial):
    historialTransformado = []
    for registro in historial:
        item = registro.copy()
        probabilidadError = random.random()
        if probabilidadError < 0.15:
            item['idHistorial'] = random.choice([None,0,-1])
            item['idUsuario'] = random.choice([None,0,-5])
        elif probabilidadError < 0.35:
            item['fechaGeneracion'] = None
        elif probabilidadError < 0.55:
            item['nombreArchivo'] = random.choice(['',None,'archivo.txt'])
        elif probabilidadError < 0.75:
            item['rutaArchivo'] = random.choice(['',None,'/ruta/invalida'])
        else:
            item['nombreArchivo'] = 'duplicado.pdf'
            item['rutaArchivo'] = '/storage/pdfs/usuarios/0/duplicado.pdf'
        historialTransformado.append(item)
    return historialTransformado