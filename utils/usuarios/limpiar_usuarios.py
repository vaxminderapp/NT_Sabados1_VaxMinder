import pandas as pd


def limpiar_usuarios(usuarios):
    if isinstance(usuarios, list):
        df = pd.DataFrame(usuarios)
    else:
        df = usuarios.copy()
    
    print("Valores nulos:")
    for col in df.columns:
        nulos = df[col].isna().sum()
        if nulos > 0:
            print(f"  {col}: {nulos}")
    
    antes = len(df)
    df = df.drop_duplicates(subset=['id_usuario'], keep='first')
    print(f"Duplicados: {antes - len(df)}\n")
    
    validos = []
    for _, fila in df.iterrows():
        if pd.isna(fila['id_usuario']) or fila['id_usuario'] <= 0:
            continue
        
        nombre = str(fila['nombre']).strip()
        if nombre == "" or nombre == "None":
            continue
        
        apellido = str(fila['apellido']).strip()
        if apellido == "" or apellido == "None":
            continue
        
        fila['nombre'] = nombre
        fila['apellido'] = apellido
        
        email = str(fila['email']).strip()
        if "@" not in email or "." not in email:
            continue
        
        contraseña = str(fila['contraseña']).strip()
        if contraseña == "" or contraseña == "None":
            continue
        
        if pd.isna(fila['fecha_nacimiento']):
            continue
        
        if pd.isna(fila['fecha_registro']):
            continue
        
        if fila['tipo_sangre'] not in ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]:
            continue
        
        telefono = str(fila['telefono']).strip()
        digitos = ""
        for c in telefono:
            if c.isdigit():
                digitos += c
        
        if len(digitos) < 7 or len(digitos) > 12:
            continue
        
        validos.append(fila)
    
    df_limpio = pd.DataFrame(validos).reset_index(drop=True)
    return df_limpio
