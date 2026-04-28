import pandas as pd


def describir_historial(df: pd.DataFrame) -> None:
    print("\n========== DESCRIPCIÓN: HISTORIAL PDF ==========")
    print(f"Número de filas:      {df.shape[0]}")
    print(f"Número de columnas:   {df.shape[1]}")
    print(f"Columnas disponibles: {list(df.columns)}")

    stats = df[['idHistorial', 'idUsuario']].describe()
    stats['idHistorial'] = stats['idHistorial'].apply(lambda x: f"{int(x)}")
    stats['idUsuario']   = stats['idUsuario'].apply(lambda x: f"{int(x)}")
    print(f"\nEstadísticas numéricas:\n{stats}")

    print(f"\nFecha mínima de generación: {df['fechaGeneracion'].min()}")
    print(f"Fecha máxima de generación: {df['fechaGeneracion'].max()}")
    print(f"\nValores nulos por columna:\n{df.isnull().sum().to_string()}")