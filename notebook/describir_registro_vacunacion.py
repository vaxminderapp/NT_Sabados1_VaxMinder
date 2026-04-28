import pandas as pd


def describir_registro_vacunacion(df: pd.DataFrame) -> None:
    print("\n========== DESCRIPCIÓN: REGISTRO VACUNACIÓN ==========")
    print(f"Número de filas:      {df.shape[0]}")
    print(f"Número de columnas:   {df.shape[1]}")
    print(f"Columnas disponibles: {list(df.columns)}")

    stats = df[['idRegistro', 'idUsuario', 'idVacuna', 'numeroDosis']].describe()
    # IDs sin separadores, dosis como enteros sin decimales
    stats['idRegistro']   = stats['idRegistro'].apply(lambda x: f"{int(x)}")
    stats['idUsuario']    = stats['idUsuario'].apply(lambda x: f"{int(x)}")
    stats['idVacuna']     = stats['idVacuna'].apply(lambda x: f"{int(x)}")
    stats['numeroDosis']  = stats['numeroDosis'].apply(lambda x: f"{int(round(x))}")
    print(f"\nEstadísticas numéricas:\n{stats}")

    print(f"\nDistribución por número de dosis:\n{df['numeroDosis'].value_counts().sort_index()}")
    print(f"\nFecha mínima de aplicación: {df['fechaAplicacion'].min()}")
    print(f"Fecha máxima de aplicación: {df['fechaAplicacion'].max()}")
    print(f"\nValores nulos por columna:\n{df.isnull().sum().to_string()}")