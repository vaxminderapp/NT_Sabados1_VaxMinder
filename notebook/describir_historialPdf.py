import pandas as pd


def describir_historial(df: pd.DataFrame) -> None:
    print("\n========== DESCRIPCIÓN: HISTORIAL PDF ==========")
    print(f"Total de documentos generados: {df.shape[0]}")

    print("\n--- Listado de documentos ---")
    print(f"  {'ID':>4}  {'ID Usuario':>12}  {'Fecha Generación':<20}  {'Archivo'}")
    print(f"  {'--':>4}  {'----------':>12}  {'----------------':<20}  {'-------'}")
    for _, fila in df.iterrows():
        print(f"  {int(fila['idHistorial']):>4}  {int(fila['idUsuario']):>12}  {str(fila['fechaGeneracion']):<20}  {fila['nombreArchivo']}")

    print(f"\n--- Período de generación ---")
    print(f"  Documento más antiguo: {df['fechaGeneracion'].min()}")
    print(f"  Documento más reciente: {df['fechaGeneracion'].max()}")

    docs_por_usuario = df.groupby('idUsuario').size()
    print(f"\n--- Documentos por usuario ---")
    for id_usuario, cantidad in docs_por_usuario.items():
        print(f"  Usuario {int(id_usuario)}: {cantidad} documento(s)")

    nulos = df.isnull().sum()
    nulos = nulos[nulos > 0]
    if not nulos.empty:
        print(f"\n--- Campos con datos faltantes ---")
        for campo, cantidad in nulos.items():
            print(f"  {campo}: {cantidad} registros sin dato")
    else:
        print("\n  Sin campos con datos faltantes.")