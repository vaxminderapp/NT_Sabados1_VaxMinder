import pandas as pd


def describir_centros_medicos(centros_df):
    """
    Realiza 3 consultas diferentes usando query() para analizar centros médicos.
    
    Args:
        centros_df (pd.DataFrame): DataFrame con datos de centros limpios
    
    Returns:
        dict: Diccionario con 3 consultas y sus resultados
    """
    
    # CONSULTA 1: Centros de tipo "Hospital"
    print("=" * 60)
    print("CONSULTA 1: Todos los Hospitales")
    print("=" * 60)
    hospitales = centros_df.query('tipo_centro == "Hospital"')
    print(f"Total de Hospitales: {len(hospitales)}")
    print(hospitales)
    print()
    
    # CONSULTA 2: Centros ubicados en Bogotá
    print("=" * 60)
    print("CONSULTA 2: Centros médicos en Bogotá")
    print("=" * 60)
    centros_bogota = centros_df.query('ciudad == "Bogotá"')
    print(f"Total de centros en Bogotá: {len(centros_bogota)}")
    print(centros_bogota)
    print()
    
    # CONSULTA 3: Centros de tipo "Clínica" que están en Medellín o Cali
    print("=" * 60)
    print("CONSULTA 3: Clínicas en Medellín o Cali")
    print("=" * 60)
    clinicas_medellin_cali = centros_df.query('tipo_centro == "Clínica" and (ciudad == "Medellín" or ciudad == "Cali")')
    print(f"Total de clínicas en Medellín o Cali: {len(clinicas_medellin_cali)}")
    print(clinicas_medellin_cali)
    print()
    
    # Retornar resultados en un diccionario
    resultados = {
        "hospitales": hospitales,
        "centros_bogota": centros_bogota,
        "clinicas_medellin_cali": clinicas_medellin_cali
    }
    
    return resultados


if __name__ == "__main__":
    from simular_centros_medicos import simular_centros_medicos
    from transformar_centros_medicos import transformar_centros_medicos
    from limpiar_centros_medicos import limpiar_centros_medicos
    
    # Simular datos
    centros_simulados = simular_centros_medicos(10)
    
    # Transformar (agregar errores)
    centros_transformados = transformar_centros_medicos(centros_simulados)
    
    # Limpiar
    centros_limpios, nulos = limpiar_centros_medicos(centros_transformados)
    
    # Describir (hacer consultas)
    resultados = describir_centros_medicos(centros_limpios)
