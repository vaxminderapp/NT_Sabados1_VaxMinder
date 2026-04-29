import pandas as pd


def describir_usuarios(df: pd.DataFrame) -> None:
    print("\n========== DESCRIPCIÓN: USUARIOS ==========")
    print(f"Número de filas:      {df.shape[0]}")
    print(f"Número de columnas:   {df.shape[1]}")
    print(f"Columnas disponibles: {list(df.columns)}")

    col_numericas   = df.select_dtypes(include='number').columns.tolist()
    col_categoricas = df.select_dtypes(include='object').columns.tolist()
    print(f"\nColumnas numéricas:   {col_numericas}")
    print(f"Columnas categóricas: {col_categoricas}")

    print(f"\nPrimeros 5 registros:\n{df.head().to_string()}")
    print(f"\nÚltimos 5 registros:\n{df.tail().to_string()}")

    print("\nEstructura del DataFrame:")
    df.info()

    stats = df[['id_usuario']].describe()
    stats['id_usuario'] = stats['id_usuario'].apply(lambda x: f"{int(x)}" if pd.notna(x) else "-")
    print(f"\nEstadísticas numéricas:\n{stats}")

    print(f"\nDistribución por tipo de sangre:\n{df['tipo_sangre'].value_counts().sort_index()}")
    print(f"\nFecha mínima de nacimiento: {df['fecha_nacimiento'].min()}")
    print(f"Fecha máxima de nacimiento: {df['fecha_nacimiento'].max()}")
    print(f"\nFecha mínima de registro: {df['fecha_registro'].min()}")
    print(f"Fecha máxima de registro: {df['fecha_registro'].max()}")
    print(f"\nValores nulos por columna:\n{df.isnull().sum().to_string()}")
