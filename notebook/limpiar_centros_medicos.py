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
        if nombre == "" or nombre.lower() in {"none", "nan"}:
            continue
        
        # Ciudad es obligatoria y no puede estar vacía
        if pd.isna(fila['ciudad']):
            continue
        ciudad = str(fila['ciudad']).strip()
        if ciudad == "" or ciudad.lower() in {"none", "nan"}:
            continue
        fila['ciudad'] = ciudad.title()
        
        # Dirección es obligatoria y no puede estar vacía
        if pd.isna(fila['direccion']):
            continue
        direccion = str(fila['direccion']).strip()
        if direccion == "" or direccion.lower() in {"none", "nan"}:
            continue
        fila['direccion'] = direccion
        
        fila['nombre_centro'] = nombre
        
        # Teléfono debe tener al menos 7 dígitos
        if pd.isna(fila['telefono']):
            continue
        telefono = str(fila['telefono']).strip()
        if telefono == "" or telefono.lower() in {"none", "nan"}:
            continue
        digitos = "".join(c for c in telefono if c.isdigit())
        if len(digitos) < 7:
            continue
        
        # Tipo de centro es obligatorio y debe ser válido
        if pd.isna(fila['tipo_centro']):
            continue
        tipo_centro = str(fila['tipo_centro']).strip()
        if tipo_centro == "" or tipo_centro.lower() in {"none", "nan"}:
            continue
        # Aceptar variaciones con y sin tildes
        tipos_validos = ["Hospital", "Clínica", "Clinica", "Centro de salud"]
        if tipo_centro not in tipos_validos:
            continue
        
        validos.append(fila)
    
<<<<<<< HEAD
=======
<<<<<<< Updated upstream
=======
>>>>>>> 41b6f2d (fix Cambios en main)
    print(f"--- Resumen limpieza centros médicos ---")
    print(f"Registros originales:  {antes}")
    print(f"Registros eliminados:  {antes - len(validos)}")
    print(f"Registros válidos:     {len(validos)}\n")

    if not validos:
        return df.iloc[0:0].reset_index(drop=True)
<<<<<<< HEAD
=======
    
>>>>>>> Stashed changes
>>>>>>> 41b6f2d (fix Cambios en main)
    df_limpio = pd.DataFrame(validos).reset_index(drop=True)
    
    # Eliminar cualquier fila que contenga NaN
    df_limpio = df_limpio.dropna()
    
    return df_limpio
