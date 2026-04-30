import pandas as pd


def limpiar_registro_vacunacion(datos):
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
    df = df.drop_duplicates(subset=['idRegistro'], keep='first')
    print(f"Duplicados: {antes - len(df)}\n")

    validos = []
    for _, fila in df.iterrows():
        if pd.isna(fila['idRegistro']) or fila['idRegistro'] <= 0:
            continue
        if pd.isna(fila['idUsuario']) or fila['idUsuario'] <= 0:
            continue
        if pd.isna(fila['fechaAplicacion']):
            continue
        numero_dosis = fila['numeroDosis']
        if pd.isna(numero_dosis) or int(numero_dosis) <= 0 or int(numero_dosis) > 10:
            continue
        lote = str(fila['loteVacuna']).strip() if not pd.isna(fila['loteVacuna']) else ''
        if not lote or len(lote) < 3:
            continue
        if pd.isna(fila['idCentroMedico']) or fila['idCentroMedico'] <= 0:
            continue
        validos.append(fila)

    print(f"--- Resumen limpieza registro vacunacion ---")
    print(f"Registros originales:  {antes}")
    print(f"Registros eliminados:  {antes - len(validos)}")
    print(f"Registros válidos:     {len(validos)}\n")

    if not validos:
        return df.iloc[0:0].reset_index(drop=True)
<<<<<<< HEAD
    return pd.DataFrame(validos).reset_index(drop=True)
=======
<<<<<<< Updated upstream
    return pd.DataFrame(validos).reset_index(drop=True)
=======
    
    df_limpio = pd.DataFrame(validos).reset_index(drop=True)
    
    # Eliminar cualquier fila que contenga NaN
    df_limpio = df_limpio.dropna()
    
    return df_limpio
>>>>>>> Stashed changes
>>>>>>> 41b6f2d (fix Cambios en main)
