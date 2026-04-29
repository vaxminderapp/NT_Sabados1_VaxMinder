import pandas as pd


def limpiar_alertas(alertas):
    if isinstance(alertas, list):
        df = pd.DataFrame(alertas)
    else:
        df = alertas.copy()
    
    print("Valores nulos:")
    for col in df.columns:
        nulos = df[col].isna().sum()
        if nulos > 0:
            print(f"  {col}: {nulos}")
    
    antes = len(df)
    df = df.drop_duplicates(subset=['id_alerta'], keep='first')
    print(f"Duplicados: {antes - len(df)}\n")
    
    validas = []
    for _, fila in df.iterrows():
        if pd.isna(fila['id_alerta']) or fila['id_alerta'] <= 0:
            continue
        if pd.isna(fila['id_usuario']) or fila['id_usuario'] <= 0:
            continue
        if fila['tipo_alerta'] not in ["refuerzo", "recordatorio", "vencimiento"]:
            continue
        if fila['estado'] not in ["pendiente", "enviada", "leida", "descartada"]:
            continue
        if pd.isna(fila['mensaje']) or str(fila['mensaje']).strip() == "":
            continue
        if pd.isna(fila['fecha_alerta']):
            continue
        
        if fila['estado'] == 'pendiente':
            fila['fecha_envio'] = None
        
        validas.append(fila)
    
    print(f"--- Resumen limpieza alertas ---")
    print(f"Registros originales:  {antes}")
    print(f"Registros eliminados:  {antes - len(validas)}")
    print(f"Registros válidos:     {len(validas)}\n")

    if not validas:
        return df.iloc[0:0].reset_index(drop=True)
    df_limpio = pd.DataFrame(validas).reset_index(drop=True)
    return df_limpio
