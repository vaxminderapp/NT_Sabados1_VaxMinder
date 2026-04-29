import pandas as pd


def limpiar_centros_medicos(centros):
    if isinstance(centros, list):
        df = pd.DataFrame(centros)
    else:
        df = centros.copy()
    
    print("Valores nulos:")
    for col in df.columns:
        nulos = df[col].isna().sum()
        if nulos > 0:
            print(f"  {col}: {nulos}")
    
    antes = len(df)
    df = df.drop_duplicates(subset=['id_centro'], keep='first')
    print(f"Duplicados: {antes - len(df)}\n")
    
    validos = []
    for _, fila in df.iterrows():
        if pd.isna(fila['id_centro']) or fila['id_centro'] <= 0:
            continue
        
        nombre = str(fila['nombre_centro']).strip()
        if nombre == "" or nombre == "None":
            continue
        
        fila['nombre_centro'] = nombre
        
        if pd.notna(fila['ciudad']):
            fila['ciudad'] = str(fila['ciudad']).strip().title()
        
        if pd.notna(fila['direccion']):
            fila['direccion'] = str(fila['direccion']).strip()
        
        telefono = str(fila['telefono']).strip()
        digitos = ""
        for c in telefono:
            if c.isdigit():
                digitos += c
        
        if len(digitos) < 7:
            continue
        
        if fila['tipo_centro'] not in ["Hospital", "Clínica", "Centro de salud"]:
            continue
        
        validos.append(fila)
    
    print(f"--- Resumen limpieza centros médicos ---")
    print(f"Registros originales:  {antes}")
    print(f"Registros eliminados:  {antes - len(validos)}")
    print(f"Registros válidos:     {len(validos)}\n")

    if not validos:
        return df.iloc[0:0].reset_index(drop=True)
    df_limpio = pd.DataFrame(validos).reset_index(drop=True)
    return df_limpio
