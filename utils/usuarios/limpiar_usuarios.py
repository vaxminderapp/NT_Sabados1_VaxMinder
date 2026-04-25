import pandas as pd


def limpiar_usuarios(usuarios):
    """
    Limpia datos de usuarios, eliminando registros inválidos, nulos y duplicados.
    
    Args:
        usuarios (list or pd.DataFrame): Datos de usuarios a limpiar
    
    Returns:
        tuple: (DataFrame limpio, reporte de nulos como diccionario)
    """
    
    # Convertir a DataFrame si es lista
    if isinstance(usuarios, list):
        df = pd.DataFrame(usuarios)
    else:
        df = usuarios.copy()
    
    # PASO 1: Reportar valores nulos por columna
    print("=" * 50)
    print("REPORTE DE VALORES NULOS")
    print("=" * 50)
    nulos_por_columna = {}
    for columna in df.columns:
        cantidad_nulos = df[columna].isna().sum()
        nulos_por_columna[columna] = cantidad_nulos
        print(f"{columna}: {cantidad_nulos} valores nulos")
    print()
    
    # PASO 2: Eliminar duplicados (basado en id_usuario)
    filas_antes = len(df)
    df = df.drop_duplicates(subset=['id_usuario'], keep='first')
    filas_despues = len(df)
    duplicados_eliminados = filas_antes - filas_despues
    print(f"Duplicados eliminados: {duplicados_eliminados}")
    print()
    
    # PASO 3: Limpiar registros (eliminar inválidos)
    usuarios_validos = []
    
    # Recorrer cada usuario
    for indice, fila in df.iterrows():
        # Validar que id_usuario sea válido
        if pd.isna(fila['id_usuario']) or fila['id_usuario'] <= 0:
            continue  # Saltar este usuario
        
        # Validar nombre no esté vacío
        nombre = str(fila['nombre']).strip()
        if nombre == "" or nombre == "None":
            continue  # Saltar este usuario
        
        # Validar apellido no esté vacío
        apellido = str(fila['apellido']).strip()
        if apellido == "" or apellido == "None":
            continue  # Saltar este usuario
        
        # Limpiar nombre y apellido
        fila['nombre'] = nombre
        fila['apellido'] = apellido
        
        # Validar email (debe tener @ y un punto)
        email = str(fila['email']).strip()
        if "@" not in email or "." not in email:
            continue  # Saltar este usuario, email inválido
        
        # Validar contraseña no esté vacía
        contraseña = str(fila['contraseña']).strip()
        if contraseña == "" or contraseña == "None":
            continue  # Saltar este usuario
        
        # Validar fecha_nacimiento no sea nula
        if pd.isna(fila['fecha_nacimiento']):
            continue  # Saltar este usuario
        
        # Validar fecha_registro no sea nula
        if pd.isna(fila['fecha_registro']):
            continue  # Saltar este usuario
        
        # Validar tipo_sangre
        tipos_sangre_validos = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
        if fila['tipo_sangre'] not in tipos_sangre_validos:
            continue  # Saltar este usuario
        
        # Validar teléfono (debe tener entre 7 y 12 dígitos)
        telefono = str(fila['telefono']).strip()
        # Contar solo los números
        digitos = ""
        for caracter in telefono:
            if caracter.isdigit():
                digitos = digitos + caracter
        
        if len(digitos) < 7 or len(digitos) > 12:
            continue  # Saltar este usuario, teléfono inválido
        
        # Si pasó todas las validaciones, agregar a válidos
        usuarios_validos.append(fila)
    
    # Crear DataFrame con los usuarios válidos
    df_limpio = pd.DataFrame(usuarios_validos)
    
    # Resetear índice
    df_limpio = df_limpio.reset_index(drop=True)
    
    return df_limpio, nulos_por_columna


if __name__ == "__main__":
    from simular_usuarios import simular_usuarios
    from transformar_usuarios import transformar_usuarios
    
    usuarios_simulados = simular_usuarios(10)
    usuarios_transformados = transformar_usuarios(usuarios_simulados)
    
    print("Usuarios transformados (con errores):")
    print(usuarios_transformados)
    
    usuarios_limpios = limpiar_usuarios(usuarios_transformados)
    print("\nUsuarios limpios:")
    print(usuarios_limpios)
