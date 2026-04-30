import pandas as pd


def limpiar_usuarios(usuarios):
    if isinstance(usuarios, list):
        df = pd.DataFrame(usuarios)
    else:
        df = usuarios.copy()
    
    print("Valores nulos en datos originales:")
    for col in df.columns:
        nulos = df[col].isna().sum()
        if nulos > 0:
            print(f"  {col}: {nulos}")
    if df.isna().sum().sum() == 0:
        print("  Ninguno")
    
    antes = len(df)
    df = df.drop_duplicates(subset=['id_usuario'], keep='first')
    print(f"Duplicados: {antes - len(df)}\n")
    
    validos = []
    for _, fila in df.iterrows():
        if pd.isna(fila['id_usuario']) or fila['id_usuario'] <= 0:
            continue
        
        if pd.isna(fila['nombre']):
            continue
        nombre = str(fila['nombre']).strip()
        if nombre == "" or nombre.lower() in {"none", "nan"}:
            continue
        
        if pd.isna(fila['apellido']):
            continue
        apellido = str(fila['apellido']).strip()
        if apellido == "" or apellido.lower() in {"none", "nan"}:
            continue
        
        fila['nombre'] = nombre
        fila['apellido'] = apellido
        
        if pd.isna(fila['email']):
            continue
        email = str(fila['email']).strip()
        if email == "" or email.lower() in {"none", "nan"}:
            continue
        if "@" not in email or "." not in email:
            continue
        if email.startswith("@") or email.endswith("@"):
            continue
        local, _, dominio = email.partition("@")
        if local.strip() == "" or "." not in dominio:
            continue
        
        if pd.isna(fila['contraseña']):
            continue
        contraseña = str(fila['contraseña']).strip()
        if contraseña == "" or contraseña.lower() in {"none", "nan"}:
            continue
        
        if pd.isna(fila['fecha_nacimiento']):
            continue
        
        if pd.isna(fila['fecha_registro']):
            continue
        
        if fila['tipo_sangre'] not in ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]:
            continue
        
        if pd.isna(fila['telefono']):
            continue
        telefono = str(fila['telefono']).strip()
        if telefono.lower() == "nan" or telefono.lower() == "none":
            continue
        if any(c.isalpha() for c in telefono):
            continue
        digitos = "" 
        for c in telefono:
            if c.isdigit():
                digitos += c
        
        if len(digitos) < 7 or len(digitos) > 12:
            continue
        
        validos.append(fila)
    
<<<<<<< HEAD
    print(f"--- Resumen limpieza usuarios ---")
    print(f"Registros originales:  {antes}")
    print(f"Registros eliminados:  {antes - len(validos)}")
    print(f"Registros válidos:     {len(validos)}\n")

    if not validos:
        return df.iloc[0:0].reset_index(drop=True)
=======
<<<<<<< Updated upstream
>>>>>>> 41b6f2d (fix Cambios en main)
    df_limpio = pd.DataFrame(validos).reset_index(drop=True)
=======
    print(f"--- Resumen limpieza usuarios ---")
    print(f"Registros originales:  {antes}")
    print(f"Registros eliminados:  {antes - len(validos)}")
    print(f"Registros válidos:     {len(validos)}\n")

    if not validos:
        df_limpio = df.iloc[0:0].reset_index(drop=True)
    else:
        df_limpio = pd.DataFrame(validos).reset_index(drop=True)

    print("Valores nulos en datos limpios:")
    nulls_final = df_limpio.isna().sum()
    if nulls_final.sum() == 0:
        print("  Ninguno")
    else:
        for col, nulos in nulls_final.items():
            if nulos > 0:
                print(f"  {col}: {nulos}")
    print()
>>>>>>> Stashed changes
    return df_limpio
