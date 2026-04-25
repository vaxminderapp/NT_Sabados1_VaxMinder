import pandas as pd


def limpiar_centros_medicos(centros):
    """
    Limpia datos de centros médicos, eliminando registros inválidos, nulos y duplicados.
    
    Args:
        centros (list or pd.DataFrame): Datos de centros a limpiar
    
    Returns:
        tuple: (DataFrame limpio, reporte de nulos como diccionario)
    """
    
    # Convertir a DataFrame si es lista
    if isinstance(centros, list):
        df = pd.DataFrame(centros)
    else:
        df = centros.copy()
    
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
    
    # PASO 2: Eliminar duplicados (basado en id_centro)
    filas_antes = len(df)
    df = df.drop_duplicates(subset=['id_centro'], keep='first')
    filas_despues = len(df)
    duplicados_eliminados = filas_antes - filas_despues
    print(f"Duplicados eliminados: {duplicados_eliminados}")
    print()
    
    # PASO 3: Limpiar registros (eliminar inválidos)
    centros_validos = []
    
    # Recorrer cada centro
    for indice, fila in df.iterrows():
        # Validar que id_centro sea válido
        if pd.isna(fila['id_centro']) or fila['id_centro'] <= 0:
            continue  # Saltar este centro
        
        # Validar nombre_centro no esté vacío
        nombre = str(fila['nombre_centro']).strip()
        if nombre == "" or nombre == "None":
            continue  # Saltar este centro
        
        # Limpiar nombre (eliminar espacios extra)
        fila['nombre_centro'] = nombre
        
        # Limpiar ciudad (eliminar espacios y capitalizar)
        if pd.notna(fila['ciudad']):
            ciudad = str(fila['ciudad']).strip()
            fila['ciudad'] = ciudad.title()  # Convertir a formato: Primera Letra Mayúscula
        
        # Limpiar dirección
        if pd.notna(fila['direccion']):
            fila['direccion'] = str(fila['direccion']).strip()
        
        # Validar teléfono (debe tener al menos 7 dígitos)
        telefono = str(fila['telefono']).strip()
        # Contar solo los números
        digitos = ""
        for caracter in telefono:
            if caracter.isdigit():
                digitos = digitos + caracter
        
        if len(digitos) < 7:
            continue  # Saltar este centro, teléfono inválido
        
        # Validar tipo_centro
        tipos_validos = ["Hospital", "Clínica", "Centro de salud"]
        if fila['tipo_centro'] not in tipos_validos:
            continue  # Saltar este centro
        
        # Si pasó todas las validaciones, agregar a válidos
        centros_validos.append(fila)
    
    # Crear DataFrame con los centros válidos
    df_limpio = pd.DataFrame(centros_validos)
    
    # Resetear índice
    df_limpio = df_limpio.reset_index(drop=True)
    
    return df_limpio, nulos_por_columna


if __name__ == "__main__":
    from simular_centros_medicos import simular_centros_medicos
    from transformar_centros_medicos import transformar_centros_medicos
    
    centros_simulados = simular_centros_medicos(10)
    centros_transformados = transformar_centros_medicos(centros_simulados)
    
    print("Centros transformados (con errores):")
    print(centros_transformados)
    
    centros_limpios = limpiar_centros_medicos(centros_transformados)
    print("\nCentros limpios:")
    print(centros_limpios)
