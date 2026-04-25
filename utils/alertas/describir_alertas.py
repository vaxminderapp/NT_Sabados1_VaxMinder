import pandas as pd


def describir_alertas(alertas_df):
    """
    Realiza 3 consultas diferentes usando query() para analizar alertas.
    
    Args:
        alertas_df (pd.DataFrame): DataFrame con datos de alertas limpios
    
    Returns:
        dict: Diccionario con 3 consultas y sus resultados
    """
    
    # CONSULTA 1: Alertas con estado "enviada"
    print("=" * 60)
    print("CONSULTA 1: Alertas que fueron enviadas")
    print("=" * 60)
    alertas_enviadas = alertas_df.query('estado == "enviada"')
    print(f"Total de alertas enviadas: {len(alertas_enviadas)}")
    print(alertas_enviadas)
    print()
    
    # CONSULTA 2: Alertas de tipo "refuerzo" que aún están "pendiente"
    print("=" * 60)
    print("CONSULTA 2: Alertas de refuerzo pendientes de envío")
    print("=" * 60)
    alertas_refuerzo_pendiente = alertas_df.query('tipo_alerta == "refuerzo" and estado == "pendiente"')
    print(f"Total de alertas de refuerzo pendiente: {len(alertas_refuerzo_pendiente)}")
    print(alertas_refuerzo_pendiente)
    print()
    
    # CONSULTA 3: Alertas de tipo "vencimiento" con estado "leida"
    print("=" * 60)
    print("CONSULTA 3: Alertas de vencimiento que fueron leídas")
    print("=" * 60)
    alertas_vencimiento_leida = alertas_df.query('tipo_alerta == "vencimiento" and estado == "leida"')
    print(f"Total de alertas de vencimiento leídas: {len(alertas_vencimiento_leida)}")
    print(alertas_vencimiento_leida)
    print()
    
    # Retornar resultados en un diccionario
    resultados = {
        "alertas_enviadas": alertas_enviadas,
        "alertas_refuerzo_pendiente": alertas_refuerzo_pendiente,
        "alertas_vencimiento_leida": alertas_vencimiento_leida
    }
    
    return resultados


if __name__ == "__main__":
    from simular_alertas import simular_alertas
    from transformar_alertas import transformar_alertas
    from limpiar_alertas import limpiar_alertas
    
    # Simular datos
    alertas_simuladas = simular_alertas(10)
    
    # Transformar (agregar errores)
    alertas_transformadas = transformar_alertas(alertas_simuladas)
    
    # Limpiar
    alertas_limpias, nulos = limpiar_alertas(alertas_transformadas)
    
    # Describir (hacer consultas)
    resultados = describir_alertas(alertas_limpias)
