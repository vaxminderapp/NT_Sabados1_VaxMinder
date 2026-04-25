import pandas as pd


def describir_usuarios(usuarios_df):
    """
    Realiza 3 consultas diferentes usando query() para analizar usuarios.
    
    Args:
        usuarios_df (pd.DataFrame): DataFrame con datos de usuarios limpios
    
    Returns:
        dict: Diccionario con 3 consultas y sus resultados
    """
    
    # CONSULTA 1: Usuarios con tipo de sangre "O+"
    print("=" * 60)
    print("CONSULTA 1: Usuarios con tipo de sangre O+")
    print("=" * 60)
    usuarios_o_positivo = usuarios_df.query('tipo_sangre == "O+"')
    print(f"Total de usuarios con O+: {len(usuarios_o_positivo)}")
    print(usuarios_o_positivo)
    print()
    
    # CONSULTA 2: Usuarios que se registraron en febrero de 2026
    print("=" * 60)
    print("CONSULTA 2: Usuarios registrados en febrero 2026")
    print("=" * 60)
    usuarios_febrero = usuarios_df.query('fecha_registro.str.contains("2026-02", na=False)')
    print(f"Total de usuarios registrados en febrero: {len(usuarios_febrero)}")
    print(usuarios_febrero)
    print()
    
    # CONSULTA 3: Usuarios con tipo de sangre AB (tanto AB+ como AB-)
    print("=" * 60)
    print("CONSULTA 3: Usuarios con tipo de sangre AB")
    print("=" * 60)
    usuarios_ab = usuarios_df.query('tipo_sangre == "AB+" or tipo_sangre == "AB-"')
    print(f"Total de usuarios con AB: {len(usuarios_ab)}")
    print(usuarios_ab)
    print()
    
    # Retornar resultados en un diccionario
    resultados = {
        "usuarios_o_positivo": usuarios_o_positivo,
        "usuarios_febrero": usuarios_febrero,
        "usuarios_ab": usuarios_ab
    }
    
    return resultados


if __name__ == "__main__":
    from simular_usuarios import simular_usuarios
    from transformar_usuarios import transformar_usuarios
    from limpiar_usuarios import limpiar_usuarios
    
    # Simular datos
    usuarios_simulados = simular_usuarios(10)
    
    # Transformar (agregar errores)
    usuarios_transformados = transformar_usuarios(usuarios_simulados)
    
    # Limpiar
    usuarios_limpios, nulos = limpiar_usuarios(usuarios_transformados)
    
    # Describir (hacer consultas)
    resultados = describir_usuarios(usuarios_limpios)
