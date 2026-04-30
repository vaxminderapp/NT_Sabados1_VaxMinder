import pandas as pd


def describir_centros_medicos(df: pd.DataFrame) -> None:
    print("\n========== DESCRIPCIÓN: CENTROS MÉDICOS ==========")
    print(f"Total de centros registrados: {df.shape[0]}")

    print("\n--- Centros por tipo ---")
    for tipo, cantidad in df['tipo_centro'].value_counts().items():
        print(f"  {tipo:<20}: {cantidad}")

    print("\n--- Centros por ciudad ---")
    ciudades = df['ciudad'].dropna().value_counts()
    if ciudades.empty:
        print("  (Sin información de ciudad disponible)")
    else:
        for ciudad, cantidad in ciudades.items():
            print(f"  {ciudad:<20}: {cantidad}")
    sin_ciudad = df['ciudad'].isna().sum()
    if sin_ciudad > 0:
        print(f"  (Sin ciudad registrada: {sin_ciudad} centros)")

    print("\n--- Listado completo ---")
    print(f"  {'ID':>4}  {'Nombre':<35}  {'Tipo':<20}  {'Ciudad':<15}")
    print(f"  {'--':>4}  {'------':<35}  {'----':<20}  {'------':<15}")
    for _, fila in df.iterrows():
        ciudad = fila['ciudad'] if pd.notna(fila['ciudad']) else "(sin ciudad)"
        print(f"  {int(fila['id_centro']):>4}  {fila['nombre_centro']:<35}  {fila['tipo_centro']:<20}  {ciudad:<15}")

    stats = df[['id_centro']].describe()
    stats['id_centro'] = stats['id_centro'].apply(lambda x: f"{int(x)}" if pd.notna(x) else "-")
    print(f"\nEstadísticas numéricas:\n{stats}")

    print(f"\nDistribución por tipo de centro:\n{df['tipo_centro'].value_counts().sort_index()}")
    print(f"\nDistribución por ciudad:\n{df['ciudad'].value_counts().sort_index()}")
    print(f"\nValores nulos por columna:\n{df.isnull().sum().to_string()}")
    nulos = df.isnull().sum()
    nulos = nulos[nulos > 0]
    if not nulos.empty:
        print(f"\n--- Campos con datos faltantes ---")
        for campo, cantidad in nulos.items():
            print(f"  {campo}: {cantidad} registros sin dato")

