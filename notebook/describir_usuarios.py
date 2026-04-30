import pandas as pd

<<<<<<< HEAD

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
=======
<<<<<<< Updated upstream
=======

def describir_usuarios(df: pd.DataFrame) -> None:
    print("\n========== DESCRIPCIÓN: USUARIOS ==========")
    print(f"Total de usuarios registrados: {df.shape[0]}")

    print("\n--- Distribución por tipo de sangre ---")
    for tipo, cantidad in df['tipo_sangre'].value_counts().sort_index().items():
        print(f"  {tipo:<5}: {cantidad} usuario(s)")

    print("\n--- Listado de usuarios ---")
    print(f"  {'Cédula':>12}  {'Nombre':<25}  {'Tipo Sangre':<12}  {'Nacimiento':<12}")
    print(f"  {'------':>12}  {'------':<25}  {'-----------':<12}  {'----------':<12}")
    for _, fila in df.iterrows():
        nombre_completo = f"{fila['nombre']} {fila['apellido']}"
        print(f"  {int(fila['id_usuario']):>12}  {nombre_completo:<25}  {fila['tipo_sangre']:<12}  {fila['fecha_nacimiento']:<12}")

    print(f"\n--- Período de registro ---")
    print(f"  Primer registro : {df['fecha_registro'].min()}")
    print(f"  Último registro : {df['fecha_registro'].max()}")

    nulos = df.isnull().sum()
    nulos = nulos[nulos > 0]
    if not nulos.empty:
        print(f"\n--- Campos con datos faltantes ---")
        for campo, cantidad in nulos.items():
            print(f"  {campo}: {cantidad} registros sin dato")
    else:
        print("\n  Sin campos con datos faltantes.")
>>>>>>> Stashed changes
>>>>>>> 41b6f2d (fix Cambios en main)
