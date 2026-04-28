import pandas as pd

def limpiar_usuarios(datos: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el set de datos de USUARIOS.
    - Elimina filas completamente duplicadas
    - Elimina filas donde los campos clave son nulos
    - Normaliza strings (strip de espacios)
    - Elimina columna de contraseña por seguridad (no debe mostrarse)
    """
    df = datos.copy()

    # 1. Eliminar duplicados exactos
    df = df.drop_duplicates()

    # 2. Eliminar filas con nulos en columnas clave
    columnas_clave = [col for col in df.columns if col in [
        "id_usuario", "nombre", "apellido", "email", "fecha_nacimiento"
    ]]
    if columnas_clave:
        df = df.dropna(subset=columnas_clave)

    # 3. Normalizar strings
    columnas_str = df.select_dtypes(include="object").columns
    for col in columnas_str:
        df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

    # 4. Eliminar columna de contraseña si existe (dato sensible)
    if "contraseña" in df.columns:
        df = df.drop(columns=["contraseña"])

    # 5. Resetear el índice
    df = df.reset_index(drop=True)

    return df