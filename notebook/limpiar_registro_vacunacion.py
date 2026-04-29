import pandas as pd


def limpiar_registro_vacunacion(datos):
    if isinstance(datos, list):
        df = pd.DataFrame(datos)
    else:
        df = datos.copy()
    return df.reset_index(drop=True)
