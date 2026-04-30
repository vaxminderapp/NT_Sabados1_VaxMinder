import pandas as pd

<<<<<<< HEAD

def describir_alertas(df: pd.DataFrame) -> None:
    print("\n========== DESCRIPCIÓN: ALERTAS ==========")
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

    stats = df[['id_alerta', 'id_usuario']].describe()
    stats['id_alerta']  = stats['id_alerta'].apply(lambda x: f"{int(x)}" if pd.notna(x) else "-")
    stats['id_usuario'] = stats['id_usuario'].apply(lambda x: f"{int(x)}" if pd.notna(x) else "-")
    print(f"\nEstadísticas numéricas:\n{stats}")

    print(f"\nDistribución por tipo de alerta:\n{df['tipo_alerta'].value_counts().sort_index()}")
    print(f"\nDistribución por estado:\n{df['estado'].value_counts().sort_index()}")
    print(f"\nFecha mínima de alerta: {df['fecha_alerta'].min()}")
    print(f"Fecha máxima de alerta: {df['fecha_alerta'].max()}")
    print(f"\nValores nulos por columna:\n{df.isnull().sum().to_string()}")
=======
<<<<<<< Updated upstream
=======

def describir_alertas(df: pd.DataFrame) -> None:
    print("\n========== DESCRIPCIÓN: ALERTAS ==========")
    print(f"Total de alertas registradas: {df.shape[0]}")
    print(f"Campos disponibles:           {list(df.columns)}")

    print("\n--- Estado de las alertas ---")
    for estado, cantidad in df['estado'].value_counts().items():
        porcentaje = cantidad / len(df) * 100
        print(f"  {estado:<12}: {cantidad} alertas ({porcentaje:.0f}%)")

    print("\n--- Tipo de alerta ---")
    for tipo, cantidad in df['tipo_alerta'].value_counts().items():
        print(f"  {tipo:<15}: {cantidad} alertas")

    pendientes = df[df['estado'] == 'pendiente']
    if not pendientes.empty:
        print(f"\n--- Alertas pendientes de envío ({len(pendientes)}) ---")
        print(f"  {'ID':>5}  {'Tipo':<15}  {'Fecha':<12}")
        print(f"  {'---':>5}  {'----':<15}  {'-----':<12}")
        for _, fila in pendientes.iterrows():
            print(f"  {int(fila['id_alerta']):>5}  {fila['tipo_alerta']:<15}  {fila['fecha_alerta']:<12}")

    print(f"\n--- Período cubierto ---")
    print(f"  Alerta más antigua : {df['fecha_alerta'].min()}")
    print(f"  Alerta más reciente: {df['fecha_alerta'].max()}")

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
