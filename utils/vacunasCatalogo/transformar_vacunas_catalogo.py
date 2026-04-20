import random
from simular_vacunas_catalogo import simular_vacunas_catalogo


def transformar_vacunas_catalogo(vacunas):
    vacunasTransformadas = []
    for vacuna in vacunas:
        item = vacuna.copy()
        probabilidadError = random.random()
        if probabilidadError < 0.15:
            item['id_vacuna'] = random.choice([None,0,-1])
        elif probabilidadError < 0.35:
            item['nombre_vacuna'] = random.choice(['',None,'   '])
        elif probabilidadError < 0.55:
            item['dosis_requeridas'] = random.choice([0,-1,25])
        elif probabilidadError < 0.75:
            item['intervalo_dosis_dias'] = random.choice([-10,None,9999])
        else:
            item['requiere_refuerzo'] = random.choice(['si','no',None])
            item['descripcion'] = random.choice(['',None])
        vacunasTransformadas.append(item)
    return vacunasTransformadas