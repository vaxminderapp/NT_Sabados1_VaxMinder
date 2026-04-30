import pandas as pd


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
    fecha_min = str(df['fecha_registro'].min()).replace(' 00:00:00','')
    print(f"  Primer registro : {fecha_min if pd.notna(fecha_min) else '(sin dato)'}")
    fecha_max = str(df['fecha_registro'].max()).replace(' 00:00:00','')
    print(f"  Último registro : {fecha_max if pd.notna(fecha_max) else '(sin dato)'}")

    nulos = df.isnull().sum()
    nulos = nulos[nulos > 0]
    if not nulos.empty:
        print(f"\n--- Campos con datos faltantes ---")
        for campo, cantidad in nulos.items():
            print(f"  {campo}: {cantidad} registros sin dato")
    else:
        print("\n  Sin campos con datos faltantes.")