import pandas as pd


def limpiar_alertas(alertas):
    """
    Limpia datos de alertas, eliminando registros inválidos, nulos y duplicados.
    
    Args:
        alertas (list or pd.DataFrame): Datos de alertas a limpiar
    
    Returns:
        tuple: (DataFrame limpio, reporte de nulos como diccionario)
    """
    
    # Convertir a DataFrame si es lista
    if isinstance(alertas, list):
        df = pd.DataFrame(alertas)
    else:
        df = alertas.copy()
    
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
    
    # PASO 2: Eliminar duplicados (basado en id_alerta)
    filas_antes = len(df)
    df = df.drop_duplicates(subset=['id_alerta'], keep='first')
    filas_despues = len(df)
    duplicados_eliminados = filas_antes - filas_despues
    print(f"Duplicados eliminados: {duplicados_eliminados}")
    print()
    
    # PASO 3: Limpiar registros (eliminar inválidos)
    alertas_validas = []
    
    # Recorrer cada alerta
    for indice, fila in df.iterrows():
        # Validar que id_alerta sea válido (no nulo y mayor a 0)
        if pd.isna(fila['id_alerta']) or fila['id_alerta'] <= 0:
            continue  # Saltar esta alerta, no es válida
        
        # Validar que id_usuario sea válido
        if pd.isna(fila['id_usuario']) or fila['id_usuario'] <= 0:
            continue  # Saltar esta alerta
        
        # Validar tipo_alerta
        tipos_validos = ["refuerzo", "recordatorio", "vencimiento"]
        if fila['tipo_alerta'] not in tipos_validos:
            continue  # Saltar esta alerta
        
        # Validar estado
        estados_validos = ["pendiente", "enviada", "leida", "descartada"]
        if fila['estado'] not in estados_validos:
            continue  # Saltar esta alerta
        
        # Validar mensaje no esté vacío
        mensaje = str(fila['mensaje']).strip()
        if mensaje == "" or mensaje == "None":
            continue  # Saltar esta alerta
        
        # Validar que fecha_alerta no sea nula
        if pd.isna(fila['fecha_alerta']):
            continue  # Saltar esta alerta
        
        # Si estado es "pendiente", la fecha_envio debe ser None
        if fila['estado'] == 'pendiente':
            fila['fecha_envio'] = None
        
        # Si pasó todas las validaciones, agregar a válidas
        alertas_validas.append(fila)
    
    # Crear DataFrame con las alertas válidas
    df_limpio = pd.DataFrame(alertas_validas)
    
    # Resetear índice
    df_limpio = df_limpio.reset_index(drop=True)
    
    return df_limpio, nulos_por_columna


if __name__ == "__main__":
    from simular_alertas import simular_alertas
    from transformar_alertas import transformar_alertas
    
    alertas_simuladas = simular_alertas(10)
    alertas_transformadas = transformar_alertas(alertas_simuladas)
    
    print("Alertas transformadas (con errores):")
    print(alertas_transformadas)
    
    alertas_limpias = limpiar_alertas(alertas_transformadas)
    print("\nAlertas limpias:")
    print(alertas_limpias)
