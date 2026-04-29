import pandas as pd


def limpiar_historial(datos):
    if isinstance(datos, list):
        df = pd.DataFrame(datos)
    else:
        df = datos.copy()

    print("Valores nulos:")
    for col in df.columns:
        nulos = df[col].isna().sum()
        if nulos > 0:
            print(f"  {col}: {nulos}")

    antes = len(df)
    df = df.drop_duplicates(subset=['idHistorial'], keep='first')
    print(f"Duplicados: {antes - len(df)}\n")

    validos = []
    for _, fila in df.iterrows():
        if pd.isna(fila['idHistorial']) or fila['idHistorial'] <= 0:
            continue
        if pd.isna(fila['idUsuario']) or fila['idUsuario'] <= 0:
            continue
        if pd.isna(fila['fechaGeneracion']):
            continue
        nombre = str(fila['nombreArchivo']).strip() if not pd.isna(fila['nombreArchivo']) else ''
        if not nombre or not nombre.endswith('.pdf'):
            continue
        ruta = str(fila['rutaArchivo']).strip() if not pd.isna(fila['rutaArchivo']) else ''
        if not ruta or ruta in ['/ruta/invalida', '/storage/pdfs/usuarios/0/duplicado.pdf']:
            continue
        validos.append(fila)

    print(f"--- Resumen limpieza historial PDF ---")
    print(f"Registros originales:  {antes}")
    print(f"Registros eliminados:  {antes - len(validos)}")
    print(f"Registros válidos:     {len(validos)}\n")

    if not validos:
        return df.iloc[0:0].reset_index(drop=True)
    return pd.DataFrame(validos).reset_index(drop=True)
