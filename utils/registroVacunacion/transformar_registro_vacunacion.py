import random
from utils.registroVacunacion.simular_registro_vacunacion import simularRegistroVacunacion


def transformar_registro_vacunacion(registros):
    registrosTransformados = []
    for registro in registros:
        item = registro.copy()
        probabilidadError = random.random()
        if probabilidadError < 0.15:
            item['idRegistro'] = random.choice([None,0,-1])
        elif probabilidadError < 0.35:
            item['fechaAplicacion'] = None
            item['proximaDosisfecha'] = None
        elif probabilidadError < 0.55:
            item['numeroDosis'] = random.choice([0,-1,99])
        elif probabilidadError < 0.75:
            item['loteVacuna'] = random.choice(['',None,'xx'])
        else:
            item['idUsuario'] = random.choice([None,-2])
            item['idCentroMedico'] = random.choice([None,-3])
        registrosTransformados.append(item)
    return registrosTransformados