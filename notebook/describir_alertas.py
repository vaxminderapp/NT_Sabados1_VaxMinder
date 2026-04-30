import pandas as pd


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
