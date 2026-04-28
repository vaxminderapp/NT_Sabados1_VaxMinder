import pandas as pd
from notebook.limpiar_alertas import limpiar_alertas as _base

def limpiar_centros_medicos(datos: pd.DataFrame) -> pd.DataFrame:
    return _base(datos)