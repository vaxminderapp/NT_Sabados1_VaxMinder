import pandas as pd


def limpiar_vacunas_catalogo(datos):
<<<<<<< HEAD
=======
<<<<<<< Updated upstream
    return _base(datos)
=======
>>>>>>> 41b6f2d (fix Cambios en main)
    if isinstance(datos, list):
        df = pd.DataFrame(datos)
    else:
        df = datos.copy()
<<<<<<< HEAD
    return df.reset_index(drop=True)
=======
    
    print("Valores nulos:")
    nulos_totales = 0
    for col in df.columns:
        nulos = df[col].isna().sum()
        if nulos > 0:
            print(f"  {col}: {nulos}")
            nulos_totales += nulos
    if nulos_totales == 0:
        print("  Ninguno")
    
    antes = len(df)
    
    # Eliminar duplicados por id_vacuna si existe
    if 'id_vacuna' in df.columns:
        df = df.drop_duplicates(subset=['id_vacuna'], keep='first')
    print(f"Duplicados: {antes - len(df)}\n")
    
    # Eliminar cualquier fila que contenga NaN
    df = df.dropna()
    
    print(f"--- Resumen limpieza vacunas catalogo ---")
    print(f"Registros originales:  {antes}")
    print(f"Registros eliminados:  {antes - len(df)}")
    print(f"Registros validos:     {len(df)}\n")
    
    return df.reset_index(drop=True)
>>>>>>> Stashed changes
>>>>>>> 41b6f2d (fix Cambios en main)
