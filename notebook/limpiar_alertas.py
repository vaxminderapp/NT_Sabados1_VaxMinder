import pandas as pd

def limpiar_alertas(datos: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el set de datos de ALERTAS.
    - Elimina filas completamente duplicadas
    - Elimina filas donde los campos clave son nulos
    - Convierte tipos de datos correctos
    - Normaliza strings (strip de espacios)
    """
    df = datos.copy()

    # 1. Eliminar duplicados exactos
    df = df.drop_duplicates()

    # 2. Eliminar filas con nulos en columnas clave
    columnas_clave = [col for col in df.columns if col in [
        "id_alerta", "id_usuario", "tipo_alerta", "fecha_alerta", "mensaje", "estado"
    ]]
    if columnas_clave:
        df = df.dropna(subset=columnas_clave)

    # 3. Normalizar strings (eliminar espacios extras)
    columnas_str = df.select_dtypes(include="object").columns
    for col in columnas_str:
        df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

    # 4. Resetear el índice
    df = df.reset_index(drop=True)

    return df